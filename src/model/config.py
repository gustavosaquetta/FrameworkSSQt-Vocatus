import os, sys
sys.path.append(os.getcwd())
import peewee
from src.model.base import Base

from src.controller.lib.ssevolutive import evolve
from src.controller.environment import Environment
DB = Environment().db
database = DB.connect()

class Config(peewee.Model, Base):

	empresa		= peewee.CharField(null=True)
	chave		= peewee.CharField(null=True)
	tipo		= peewee.CharField(null=True)
	valor		= peewee.TextField(null=True)
	descricao	= peewee.TextField(null=True)
	usuario		= peewee.TextField(null=True)
	estacao		= peewee.TextField(null=True)

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
	Config.create_table()