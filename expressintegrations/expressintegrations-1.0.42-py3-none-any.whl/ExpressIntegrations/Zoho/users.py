from ..HTTP.Requests import *
from .zoho import HEADERS

BASE_URL = 'https://books.zoho.com/api/v3/users'


def create_user(user):
  result = post(BASE_URL, HEADERS, json.dumps(user))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to create user. Result: {result}")
  return result


def update_user(user_id, user):
  post_url = f"{BASE_URL}/{user_id}"
  result = put(post_url, HEADERS, json.dumps(user))
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to update user. Result: {result}")
  return result


def get_user(user_id):
  post_url = f"{BASE_URL}/{user_id}"
  result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve user. Result: {result}")
  return result


def search_users(filter_by=None, sort_column='email', **kwargs):
  # sort_column Allowed Values: name, email, user_role and status
  post_url = f"{BASE_URL}?sort_column={sort_column}"
  if filter_by is not None:
    post_url = f"{post_url}&filter_by={filter_by}"
  for name, value in kwargs.items():
    post_url = f"{post_url}&{name}={value}"
  result = get(post_url, HEADERS)
  if not Utils.is_success(result['status_code']):
    raise Exception(f"Failed to retrieve users. Result: {result}")
  return result
