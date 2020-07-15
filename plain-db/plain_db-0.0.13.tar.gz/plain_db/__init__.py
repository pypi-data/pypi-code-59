#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'plain_db'
import os

def getFile(fn, isIntValue=True):
	result = {}
	if not os.path.exists(fn):
		return result
	with open(fn) as f:
		for line in f.readlines():
			line = line.strip()
			if not line:
				continue
			if isIntValue:
				key = ' '.join(line.split()[:-1])
				value = int(line.split()[-1])
			else:
				key = line.split()[0]
				value = ' '.join(line.split()[1:])
			result[key] = value
	return result

class DB(object):
	def __init__(self, name, isIntValue=True): 
		self.fn = 'db/' + name
		self.items = getFile(self.fn, isIntValue=isIntValue)

	def update(self, key, value):
		if key not in self.items:
			self.items[key] = value
			self.appendSave(key, value)
			return
		self.items[key] = value
		self.save()

	def inc(self, key, value):
		oldValue = self.items.get(key, 0)
		self.update(key, oldValue + value)

	def get(self, key, default=None):
		return self.items.get(key) or default

	def appendSave(self, key, value):
		if len(self.items) == 1:
			with open(self.fn, 'w') as f:
				f.write(str(key) + ' ' + str(value))
			return
		with open(self.fn, 'a') as f:
			f.write('\n' + str(key) + ' ' + str(value))

	def save(self):
		lines = [key + ' ' + str(self.items[key]) for key in self.items]
		lines.sort()
		towrite = '\n'.join(lines)
		if not towrite:
			return
		os.system('mkdir db > /dev/null 2>&1')
		with open(self.fn + 'tmp', 'w') as f:
			f.write(towrite)
		os.system('mv %stmp %s' % (self.fn, self.fn))

def load(fn, isIntValue=True):
	return DB(fn, isIntValue=isIntValue)

class NoValueDB(object):
	def __init__(self, name):
		self._db = DB(name)

	def add(self, key):
		if self._db.get(key) == 1:
			return False
		self._db.update(key, 1)
		return True

	def items(self):
		return list(self._db.items.keys())

def loadKeyOnlyDB(fn):
	return NoValueDB(fn)

class LargeDB(object):
	def __init__(self, name, isIntValue=False):
		self._db = DB(name, isIntValue=isIntValue)

	def get(self, key, default):
		return self._db.get(key, default)

	def update(self, key, value):
		if self._db.get(key) == value:
			return
		self._db.items[key] = value
		self._db.appendSave(key, value)

	def items(self):
		return self._db.items.items()

	def getFn(self):
		return self._db.fn

def loadLargeDB(fn, isIntValue=False):
	return LargeDB(fn, isIntValue=isIntValue)

def cleanupLargeDB(fn):
	f1 = loadLargeDB(fn)
	f2 = loadLargeDB(fn + 'tmp')
	for key, value in f1.items():
		f2.update(key, value)
	os.system('mv %s %s' % (f2.getFn(), f1.getFn()))
