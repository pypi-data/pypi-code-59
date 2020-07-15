import os
import time
import logging
from typing import Dict

from playhouse.shortcuts import dict_to_model

from minio import Minio
from minio.error import ResponseError

from elasticsearch import Elasticsearch

from multiprocessing import Pool
from functools import partial

from zhongkui.core import File, ZhongkuiInvalidFile

from malnet.db import (Task, Sample, md52Bucket, md52Object, MALDB,
                       createSampleTable, CollectFS)

from malnet.core import Singleton, MalnetCriticalError

log = logging.getLogger(__name__)


class AnalysisClient(metaclass=Singleton):
    def __init__(self, config: Dict):
        self.config = config
        self._initClient()

    def _initClient(self):
        # postgres
        createSampleTable()
        #
        self.elasticClient = self._getElasticClient()
        self.minioClient = self._getMinioClient()

    def _getElasticClient(self):
        cfg = self.config['ELASTIC']
        return Elasticsearch(hosts=cfg['host'])

    def _getMinioClient(self):
        cfg = self.config['MINIO']
        minioClient = Minio(cfg['host'],
                            access_key=cfg['user'],
                            secret_key=cfg['password'],
                            secure=cfg['secure'])
        return minioClient


class AnalysisManager(object):
    def __init__(self, config: Dict):
        self.config = config
        self.wait = []

        self.task_count = 0
        self.task_valid = 0
        self.period_count = 0
        self.task_success = 0

    def report(self):
        log.warning(f"""{self.taskName} report:
                collect task = {self.task_count}
                valid task = {self.task_valid}
                period task = {self.period_count}
                success task={self.task_success}""")

    def produce(self, batch):
        raise NotImplementedError

    def runForever(self):
        raise NotImplementedError


class CollectAnalysisManager(AnalysisManager):
    def __init__(self, fpath, config: Dict):
        super().__init__(config)
        self.fpath = fpath
        self.taskName = 'CollectAnalysisManager'

    def produce(self, batch=200):
        for domain, package, samples in CollectFS.walk(self.fpath):
            if len(samples) != 0:
                for i in samples:
                    self.wait.append((domain, package, i))

    def runForever(self):
        # get config
        config = self.config
        rest_interval = config['COLLECT']['rest_interval']
        worker = config['COLLECT']['worker']

        # ========== concurrent stage ==================
        collectConsumerMulti = partial(collectConsumer, config=config)
        pool = Pool(processes=worker)
        # init task
        self.produce()

        while True:
            tasks = self.wait
            num_tasks = len(tasks)
            if num_tasks == 0:
                log.info(f"CollectAnalysisManager is waiting for task...")
                time.sleep(rest_interval)
                self.produce()
                continue

            self.task_count += num_tasks

            try:
                results_async = pool.map_async(collectConsumerMulti, tasks)
                results_async.wait()
                results = results_async.get()
            except Exception as e:
                log.error(f"worker pool error: {e}")
                # clear tasks
                self.wait = []
                continue

            for status in results:
                if status is not None:
                    self.task_valid += 1
                if status:
                    self.task_success += 1

            self.wait = []
            self.report()

        pool.close()


def deleteFile(fpath):
    try:
        CollectFS.delete(fpath)
    except MalnetCriticalError as e:
        log.error(e)


def collectConsumer(task, config):
    '''collect consumer'''
    pid = os.getpid()
    domain, package, sample = task
    # init client
    AC = AnalysisClient(config)

    # parse config
    includedFileType = config['COLLECT']['include_file_type']
    index = config['COLLECT']['index']
    bucket = config['COLLECT']['bucket']

    # filter fileType
    try:
        zkfile = File(sample)
    except ZhongkuiInvalidFile as e:
        log.error(f"worker-{pid} parse error {e}")
        deleteFile(sample)
        return
    if zkfile.fileType not in includedFileType:
        deleteFile(sample)
        return

    # get basicInfo
    info = zkfile.basicInfo()
    info.update({'collectDomain': domain, 'collectPackage': package})

    # get client
    elasticClient = AC.elasticClient
    minioClient = AC.minioClient

    log.info(f"worker-{pid} collecting {sample}")

    # store to Minio
    # Bucket name must follow S3 standards
    # bucket = "".join(file_type.lower().split())
    md5 = info["md5"]
    object_name = md52Object(md5)
    try:
        if not minioClient.bucket_exists(bucket):
            minioClient.make_bucket(bucket)

        minioClient.fput_object(bucket_name=bucket,
                                object_name=object_name,
                                file_path=sample)
    except ResponseError as e:
        log.error(f"worker-{pid} minio error {e}")
        return False
    log.info(f"worker-{pid} stored {md5} to Minio")

    # add to Sample
    try:
        with MALDB.atomic():
            if Sample.get_or_none(Sample.md5 == md5) is None:
                sp = dict_to_model(Sample, info)
                sp.save()
                log.info(f"worker-{pid} add {md5} to Sample")
            else:
                sp = Sample.get(Sample.md5 == md5)
                log.info(f"worker-{pid} {md5} is already collected")
    except Exception as e:
        log.error(f"worker-{pid} add {md5} to Sample error {e}")
        return False

    # add result Elastic:
    result = sp.toDict()
    try:
        if elasticClient.exists(index=index, id=md5):
            body = {'doc': result}
            elasticClient.update(index=index, id=md5, body=body)
        else:
            elasticClient.index(index=index, id=md5, body=result)
    except Exception as e:
        log.error(f"worker-{pid} save {md5} to elastic error {e}")
        return False

    # rm sample
    deleteFile(sample)
    log.info(f"worker-{pid} removed {md5}")

    return True