#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'plain_db'
import os

PIECE_LIMIT = 1024 * 1024 * 128

def getFileSingle(fn, isIntValue=True):
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

def nextPiece(piece):
	if piece == '':
		return '1'
	return str(int(piece) + 1)

def getFile(fn, isIntValue=True):
	piece = ''
	result = {}
	while True:
		tmp_filename = fn + piece
		if not os.path.exists(tmp_filename):
			return result
		tmp_result = getFileSingle(tmp_filename, isIntValue=isIntValue)
		result.update(tmp_result)
		piece = nextPiece(piece)

class DB(object):
	def __init__(self, name, isIntValue=True, default = None, 
			piece_limit = PIECE_LIMIT): 
		self.fn = 'db/' + name
		self.isIntValue = isIntValue
		self.items = getFile(self.fn, isIntValue=isIntValue)
		self.defaultValue = default
		self.current_piece = ''
		self.piece_limit = piece_limit

	def update(self, key, value):
		if key not in self.items:
			self.items[key] = value
			self.appendSave(key, value)
			return
		self.items[key] = value
		self.save()

	def remove(self, key):
		if key in self.items:
			del self.items[key]
			self.save()

	def inc(self, key, value):
		oldValue = self.items.get(key, 0)
		self.update(key, oldValue + value)

	def get(self, key, default=None):
		if key in self.items:
			return self.items[key]
		if default != None:
			return default
		return self.defaultValue

	def appendSave(self, key, value):
		current_fn = self.fn + self.current_piece
		if not os.path.exists(current_fn):
			with open(current_fn, 'w') as f:
				f.write(str(key) + ' ' + str(value))
		else:
			with open(current_fn, 'a') as f:
				f.write('\n' + str(key) + ' ' + str(value))
		if os.stat(current_fn).st_size > self.piece_limit:
			self.current_piece = nextPiece(self.current_piece)

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
		if self._db.get(key, 0) >= 1:
			return False
		self._db.update(key, 1)
		return True

	def remove(self, key):
		self._db.remove(key)

	def items(self):
		return list(self._db.items.keys())

def loadKeyOnlyDB(fn):
	return NoValueDB(fn)

class LargeDB(object):
	def __init__(self, name, isIntValue=False, 
			default=None, piece_limit=PIECE_LIMIT):
		self._db = DB(name, isIntValue=isIntValue, 
			default = default, piece_limit=piece_limit)

	def load(self):
		self._db.load()

	def get(self, key, default=None):
		return self._db.get(key, default)

	def update(self, key, value):
		if self._db.get(key) == value:
			return
		self._db.items[key] = value
		self._db.appendSave(key, value)

	def items(self):
		return list(self._db.items.items())

	def keys(self):
		for key, value in self.items():
			if value:
				yield key

	def getFn(self):
		return self._db.fn

def loadLargeDB(fn, isIntValue=False, default=None, piece_limit=PIECE_LIMIT):
	return LargeDB(fn, isIntValue=isIntValue, default = default,
		piece_limit=piece_limit)

def cleanupLargeDB(fn, piece_limit = PIECE_LIMIT):
	f1 = loadLargeDB(fn)
	f2 = loadLargeDB(fn + 'tmp', piece_limit = piece_limit)
	for key, value in f1.items():
		f2.update(key, value)
	current_piece = ''
	while True:
		if not os.path.exists(f2.getFn() + current_piece):
			break
		os.system('mv %s %s' % (f2.getFn() + current_piece, f1.getFn() + current_piece))
		current_piece = nextPiece(current_piece)
	while True:
		if not os.path.exists(f1.getFn() + current_piece):
			return
		os.system('rm %s' % (f1.getFn() + current_piece))
		current_piece = nextPiece(current_piece)