import uuid

import boto3
from botocore.config import Config
from boto3.s3.transfer import TransferConfig, S3Transfer

from pyPreservica.common import *
import requests

transfer_config = TransferConfig(use_threads=False)


class IngestAPI(AuthenticatedAPI):

    def upload_zip(self, folder: Entity, zipFile, callback=None):
        bucket = f'{self.tenant.lower()}.package.upload'
        endpoint = f'https://{self.server}/api/s3/buckets'
        client = boto3.client('s3', endpoint_url=endpoint, aws_access_key_id=self.token, aws_secret_access_key="NOT_USED",
                              config=Config(s3={'addressing_style': 'path'}))

        metadata = {'Metadata': {'structuralobjectreference': folder.reference}}
        sip_name = str(uuid.uuid4())
        transfer = S3Transfer(client, config=transfer_config)
        transfer.upload_file(zipFile, bucket, sip_name, callback=callback,  extra_args=metadata)

    def buckets(self):
        headers = {HEADER_TOKEN: self.token}
        request = requests.get(f'https://{self.server}/api/s3/buckets', headers=headers)
        if request.status_code == requests.codes.ok:
            print(request.content)
