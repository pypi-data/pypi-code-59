#!/usr/bin/python
#coding:utf-8

"""
@author: yangst2
@contact: yangst2@lenovo.com
@software: PyCharm
@file: test_cphe.py
@time: 2020/7/21 13:35
"""

import os
import zipfile
from boto3.session import Session


class CephS3Client:

    def __init__(self, access_key, secret_key, url):
        self.access_key = access_key
        self.secret_key = secret_key
        self.url = url
        self.session = self.init_session()
        self.client = self.init_client()

    def init_session(self):
        return Session(aws_access_key_id=self.access_key,
                       aws_secret_access_key=self.secret_key)

    def init_client(self):
        return self.session.client('s3', endpoint_url=self.url)

    def get_all_bucket(self):
        buckets = [bucket['Name'] for bucket in self.client.list_buckets()['Buckets']]
        return buckets

    def create_bucket(self, bucket_name=""):
        if not isinstance(bucket_name, str) or len(bucket_name.lstrip().rstrip()) == 0:
            print("Bucket name: {} is illegal ... ")
            exit()
        if bucket_name in self.get_all_bucket():
            print("Bucket name: {} has already existed ... ".format(bucket_name))
        else:
            resp = self.client.create_bucket(Bucket=bucket_name, ACL='public-read')
            if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
                print("Bucket name: {} created successfully ... ".format(bucket_name))
            else:
                print("Bucket name: {} created failure ... ".format(bucket_name))


    def upload(self, bucket_name, key, file_path):
        if not os.path.exists(file_path) or os.path.isdir(file_path):
            print("File Path : {} is a directory or doesn't exist ... ".format(file_path))
            exit()
        if bucket_name not in self.get_all_bucket():
            print("Bucket name: {} doesn't exist ... ".format(bucket_name))
            self.create_bucket(bucket_name)
        resp = self.client.put_object(
            Bucket=bucket_name, Key=key,
            Body=open(file_path, 'rb').read()
        )
        if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("File : {} upload successfully ... ".format(file_path))
        else:
            print("File : {} upload failure ... ".format(file_path))

    def download(self, bucket_name, key, file_path):
        if bucket_name not in self.get_all_bucket():
            print("Bucket name: {} doesn't exist ... ".format(bucket_name))
            exit()
        response = self.client.list_objects_v2(Bucket=bucket_name)
        object_list = [item["Key"] for item in response["Contents"]]
        if key not in object_list:
            print("Key : {} doesn't exist in {} ... ".format(key, bucket_name))
            exit()
        resp = self.client.get_object(Bucket=bucket_name, Key=key)
        dir_name = os.path.dirname(file_path)
        if not os.path.exists(dir_name) and len(dir_name) > 0:
            os.makedirs(dir_name)
        with open(file_path, 'wb') as f:
            f.write(resp['Body'].read())
        if resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
            print("File : {} download successfully ... ".format(file_path))
        else:
            print("File : {} download failure ... ".format(file_path))

    @staticmethod
    def un_zip_files(file_path):
        if file_path.endswith(".zip"):
            zip_file = zipfile.ZipFile(file_path, 'r')
            target_dir_name = file_path.replace(".zip", "")
            if not os.path.exists(target_dir_name):
                os.makedirs(target_dir_name)
            for filename in zip_file.namelist():
                data = zip_file.read(filename)
                file = open(os.path.join(target_dir_name, filename), 'w+b')
                file.write(data)
                file.close()


if __name__ == "__main__":

    pass