import os
import requests

API_URL = os.getenv('CRONO_API_URL', 'https://api.crono.com')
API_KEY = os.getenv('CRONO_API_KEY')
API_KEY_HEADER = 'X-API-Key'

class Job:

	def __init__(self, trigger=None, task=None):
		self.headers = {API_KEY_HEADER: API_KEY}
		self.trigger = trigger
		self.task = task
		self.uuid = None

	def send(self):

		if self.uuid == None and self.task != None and self.trigger != None:
			url = f'{API_URL}/jobs'
			json = {'task': self.task, 'trigger': self.trigger}
			response = requests.post(url, headers=self.headers, json=json)
			self.uuid = response.json()
			return response.json()
		
		return self

	# Jobs

	@classmethod
	def jobs(cls):
		url = f'{API_URL}/jobs'
		headers = {API_KEY_HEADER: API_KEY} # TODO cls.headers?
		response = requests.get(url, headers=headers)
		return response.json()

	@classmethod
	def job(cls, uuid):
		url = f'{API_URL}/jobs/{uuid}'
		headers = {API_KEY_HEADER: API_KEY} # TODO cls.headers?
		response = requests.get(url, headers=headers)
		return response.json()

	@classmethod
	def delete(cls, uuid):
		url = f'{API_URL}/jobs/{uuid}'
		headers = {API_KEY_HEADER: API_KEY} # TODO cls.headers?
		response = requests.delete(url, headers=headers)
		return response.json()

	# Triggers

	def on(self, *args, **kwargs):
		self.trigger = {'name': 'on', 'args': args, 'kwargs': kwargs}
		return self.send()

	def after(self, *args, **kwargs):
		self.trigger = {'name': 'after', 'args': args, 'kwargs': kwargs}
		return self.send()

	def every(self, *args, **kwargs):
		self.trigger = {'name': 'every', 'args': args, 'kwargs': kwargs}
		return self.send()

	def cron(self, *args, **kwargs):
		self.trigger = {'name': 'cron', 'args': args, 'kwargs': kwargs}
		return self.send()

	def at(self, *args, **kwargs):
		self.trigger = {'name': 'at', 'args': args, 'kwargs': kwargs}
		return self.send()

	# Tasks

	def log(self, *args, **kwargs):
		self.task = {'name': 'log', 'args': args, 'kwargs': kwargs}
		return self.send()

	def request(self, *args, **kwargs):
		self.task = {'name': 'request', 'args': args, 'kwargs': kwargs}
		return self.send()

	def message(self, *args, **kwargs):
		self.tas = {'name': 'message', 'args': args, 'kwargs': kwargs}
		return self.send()

	def email(self, *args, **kwargs):
		self.task = {'name': 'email', 'args': args, 'kwargs': kwargs}
		return self.send()
