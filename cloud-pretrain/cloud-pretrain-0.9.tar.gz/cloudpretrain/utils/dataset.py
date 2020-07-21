from __future__ import print_function, absolute_import

import click
import os
from cloudpretrain.utils.fds import check_object_exists,load_object
from cloudpretrain.config import default_config
from cloudpretrain.constants import DATASET_PREFIX, CLOUD_PRETRAIN_BUCKET, DES_FILE_NAME, DATASET_PREFIX


def is_dataset_exists(name, version, is_public, group):
    if is_public:
        bucket_name = CLOUD_PRETRAIN_BUCKET
    else:
        bucket_name = default_config.fds_bucket
    
    dataset_path = os.path.join(DATASET_PREFIX, group, name, version, DES_FILE_NAME).replace('\\', '/')

    return check_object_exists(bucket_name, dataset_path)


def load_dataset_des(name, version, is_public, group):
    if is_public:
        bucket_name = CLOUD_PRETRAIN_BUCKET
    else:
        bucket_name = default_config.fds_bucket

    dataset_path = os.path.join(DATASET_PREFIX, group, name, version, DES_FILE_NAME).replace('\\', '/')

    return load_object(bucket_name, dataset_path)


def gen_dataset_folder(name, version, is_public, group):
    return os.path.join(DATASET_PREFIX, group, name, version).replace('\\', '/')