import os, sys
sys.path.append(os.getcwd())


import peewee

from src.model.base import Base

from src.controller.lib.ssevolutive import evolve
from src.controller.environment import Environment
DB = Environment().db
database = DB.connect()

class Look(peewee.Model, Base):

	style_sheet		= peewee.IntegerField(null=True)
	look_and_feel	= peewee.IntegerField(null=True)

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
	Look.create_table()