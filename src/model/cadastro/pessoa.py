import os, sys
sys.path.append(os.getcwd())

import peewee

from src.model.base import Base

from src.controller.lib.ssevolutive import evolve
from src.controller.environment import Environment
DB = Environment().db
database = DB.connect()

class Pessoa(peewee.Model, Base):
	def __init__(self, env=None):
		super(Pessoa,self).__init__()
		if env:
			database = env.db.connect()

	nome               	= peewee.CharField(null=True)
	codigo             	= peewee.BigIntegerField(null=True)
	numero             	= peewee.IntegerField(null=True)
	atuacao            	= peewee.IntegerField(null=True)
	cep                	= peewee.CharField(null=True)
	cpf                	= peewee.CharField(null=True)
	logradouro         	= peewee.CharField(null=True)
	data_cad           	= peewee.DateField(null=True)
	apelido            	= peewee.CharField(null=True)
	bairro             	= peewee.CharField(null=True)
	cnae               	= peewee.BigIntegerField(null=True)
	complemento        	= peewee.CharField(null=True)
	inscricao_estaudual	= peewee.CharField(null=True)
	inscricao_municipal	= peewee.CharField(null=True)
	municipio          	= peewee.BigIntegerField(null=True)
	pais               	= peewee.BigIntegerField(null=True)
	pessoa_grupo       	= peewee.BigIntegerField(null=True)
	razao_social       	= peewee.CharField(null=True)

	def begin(self):
		database.begin()
		database.set_autocommit(False)
	
	def commit(self):
		database.commit()
		database.set_autocommit(True)

	def rollback(self):
		database.rollback()
		database.set_autocommit(True)

	class Meta:
		database = database

try:
	if database:
		database.evolve()
except peewee.OperationalError:
	Pessoa.create_table()
