import os, sys
sys.path.append(os.getcwd())


import peewee

from src.model.base import Base

from src.controller.environment import Environment
DB = Environment().db
database = DB.connect()

class Cliente(peewee.Model, Base):

	codigo  = peewee.CharField()
	nome 	= peewee.CharField(null=True)
	alias   = peewee.CharField(null=True)
	add     = peewee.TextField(null=True)

	def begin(self):
		database.begin()

	def commit(self):
		database.commit()

	def rollback(self):
		database.rollback()
	
	class Meta:
		database = database

try:
	if database:
		database.evolve()
except peewee.OperationalError:
	Cliente.create_table()