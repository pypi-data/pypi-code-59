'''malnet db'''
import json

from datetime import datetime
from peewee import (Model, PostgresqlDatabase, TextField, DateTimeField,
                    IntegerField, ForeignKeyField, SqliteDatabase,
                    BooleanField)

from malnet.core import Config

MALNET_CFG = Config().get()

if MALNET_CFG['MOD'] == 'dev':
    MALDB = SqliteDatabase('malnet.db')
else:
    MALNET_DB_CFG = MALNET_CFG['POSTGRES']
    MALDB = PostgresqlDatabase(MALNET_DB_CFG['name'],
                               user=MALNET_DB_CFG['user'],
                               password=MALNET_DB_CFG['password'],
                               host=MALNET_DB_CFG['host'])


class Priority:
    L0 = 0
    L1 = 1
    L2 = 2
    L3 = 3
    L4 = 4


class CollectType:
    COLLECT = 'collect'


class AnalysisType:
    STATIC = 'static'
    DYNAMIC = 'dynamic'
    VIRUSTOTAL = 'virustotal'
    PACKER = 'packer'


class ModelBase(Model):
    class Meta:
        database = MALDB


class Task(ModelBase):
    taskName = TextField(null=False, unique=True)
    description = TextField(null=True)
    analysisTool = TextField(null=True)
    toolVersion = DateTimeField(null=True)
    analyst = DateTimeField(null=True)

    class Meta:
        table_name = 'malnetTask'

    def register(self, taskName, description, analysisTool, toolVersion,
                 analyst):
        with MALDB.atomic():
            created, t = Task.get_or_create(taskName=taskName)
        if created:
            t.description = description
            t.analysisTool = analysisTool
            t.toolVersion = toolVersion
            t.analyst = analyst
            t.save()
        return t


class Sample(ModelBase):
    # index
    md5 = TextField(null=False, unique=True)
    sha1 = TextField(null=False, unique=True)
    sha256 = TextField(null=False, unique=True)
    # source
    name = TextField(null=False)
    collectDomain = TextField(null=False)
    collectPackage = TextField(null=True)
    collectTime = DateTimeField(default=datetime.now())
    # basicInfo
    fileType = TextField(null=False)
    fileSize = TextField(null=False)
    isProbablyPacked = BooleanField(default=False)
    # priority
    priority = IntegerField(default=Priority.L2)
    collectType = TextField(default=CollectType.COLLECT)

    def toDict(self, encode_date=True):
        data = {}
        for field in self._meta.sorted_fields:
            value = self.__data__.get(field.name)
            if encode_date and isinstance(value, datetime):
                value = value.strftime("%Y-%m-%d %H:%M:%S")
            data[field.name] = value
        return data

    def toJson(self):
        return json.dumps(self.toDict())

    class Meta:
        order_by = ['-priority']
        table_name = 'malnetSample'


class AnalysisModel(ModelBase):
    lastAnalysisTime = DateTimeField(null=True)

    @classmethod
    def getNewTask(cls,
                   task_id,
                   batch=1000,
                   sample_collect_type=CollectType.COLLECT):
        '''This is a very-slow-api (10-million-level batch=2000, time ~ 14s), just init with a large batch and manage tasks in memory.
            Avoid calling this API frequently !!!
        '''
        task_sample = (
            Sample.select().where(Sample.collectType == sample_collect_type) -
            Sample.select().join(cls).where(cls.task_id == 1)).limit(batch)

        return task_sample


class StaticAnalysis(AnalysisModel):
    sample = ForeignKeyField(Sample, backref='staticanalysis')
    task = ForeignKeyField(Task, backref='staticanalysis')

    class Meta:
        table_name = 'malnetStaicAnalysis'


class DynamicAnalysis(AnalysisModel):
    sample = ForeignKeyField(Sample, backref='dynamicanalysis')
    task = ForeignKeyField(Task, backref='dynamicanalysis')

    class Meta:
        table_name = 'malnetDynamicAnalysis'


class PackerAnalysis(AnalysisModel):
    sample = ForeignKeyField(Sample, backref='packeranalysis')
    task = ForeignKeyField(Task, backref='packeranalysis')

    class Meta:
        table_name = 'malnetPackerAnalysis'


class VirusTotalAnalysis(AnalysisModel):
    sample = ForeignKeyField(Sample, backref='virustotalanalysis')
    task = ForeignKeyField(Task, backref='virustotalanalysis')

    class Meta:
        table_name = 'malnetVirusTotalAnalysis'


TABLES = [
    Sample, Task, VirusTotalAnalysis, PackerAnalysis, StaticAnalysis,
    DynamicAnalysis
]


def createSampleTable():
    with MALDB:
        MALDB.create_tables(TABLES)


def dropSampleTable():
    with MALDB:
        MALDB.drop_tables(TABLES)