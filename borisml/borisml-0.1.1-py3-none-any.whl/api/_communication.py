import os
import time
import random
import requests

SERVER_LOCATION = os.getenvb(b'BORIS_SERVER_LOCATION',
                             b'https://api-dev.whattolabel.com').decode()


def _post_request(dst_url, data=None, json=None,
                  max_backoff=32, max_retries=5):

    counter = 0
    backoff = 0.05 + random.random() * 0.1
    success = False
    while not success:
        time.sleep(backoff)
        response = requests.post(dst_url, data=data, json=json)

        success = (response.status_code == 200)
        if not success:
            backoff = 2*backoff if backoff < max_backoff else backoff
            print(f'Error status_code: {response.status_code} ' +
                  f'msg: {response.text}')

        counter += 1
        if counter >= max_retries:
            break

    return response, success


def _put_request(dst_url, data,
                 max_backoff=32, max_retries=5):

    counter = 0
    backoff = 0.05 + random.random() * 0.1
    success = False
    while not success:
        time.sleep(backoff)
        response = requests.put(dst_url, data)

        success = (response.status_code == 200)
        if not success:
            backoff = 2*backoff if backoff < max_backoff else backoff
            print(f'Error status_code: {response.status_code} ' +
                  f'msg: {response.text}')

        counter += 1
        if counter >= max_retries:
            break

    return response, success


def create_initial_tag(dataset_id: str, token: str):
    """Makes empty post request to dataset to create initial tag
    
    Args:
        dataset_id: Identifier of the dataset
        token: The token for authenticating the request

    Raises:
        RuntimeError if requesting signed url failed
    """

    payload = {
        'token': token
    }
    dst_url = f'{SERVER_LOCATION}/users/datasets/{dataset_id}/tags'
    response, success = _post_request(dst_url, json=payload)
    if not success:
        raise RuntimeError('Error during creation of initial tag')


def get_presigned_upload_url(filename: str,
                             dataset_id: str,
                             token: str) -> str:
    """Creates and returns a signed url to upload an image for a specific dataset

    Args:
        filename: Name of file used for database and cloud storage
        dataset_id: Identifier of the dataset
        token: The token for authenticating the request

    Returns:
        A string containing the signed url

    Raises:
        RuntimeError if requesting signed url failed
    """

    payload = {
        'sample': {
            'fileName': filename,
        },
        'token': token
    }
    dst_url = f'{SERVER_LOCATION}/users/datasets/{dataset_id}/samples'
    response, success = _post_request(dst_url, json=payload)

    data = response.json()
    if 'error' in data.keys():
        raise RuntimeError(data['error'])

    if 'signedWriteUrl' not in data.keys():
        raise RuntimeError('url key not found')
    signed_url = data['signedWriteUrl']

    return signed_url, success


def upload_file_with_signed_url(filename: str, url: str) -> bool:
    """Upload a file to the cloud storage using a signed URL

    Args:
        filename: Path to a file for upload
        url: Signed url for push

    Returns:
        A boolean value indicating successful upload
    """
    file = open(filename, 'rb')

    response, success = _put_request(url, data=file)
    return success


def upload_embedding(data: dict) -> bool:
    """Uploads embedding

    Args:
        data: Object with embedding data

    Returns:
        A boolean value indicating successful upload
    """

    payload = {
        'embeddingName': data['embeddingName'],
        'embeddings': data['embeddings'],
        'token': data['token'],
        'append': data['append'],
    }

    dataset_id = data['datasetId']
    dst_url = f'{SERVER_LOCATION}/users/datasets/{dataset_id}/embeddings'
    response, success = _post_request(dst_url, json=payload)

    return success
