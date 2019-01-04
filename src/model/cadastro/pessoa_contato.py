'''
Created on 17 de nov de 2017

@author: gustavosaquetta
'''
	
import os, sys
sys.path.append(os.getcwd())

import peewee

from src.model.base import Base

from src.controller.lib.ssevolutive import evolve
from src.controller.environment import Environment
DB = Environment().db
database = DB.connect()

class PessoaContato(peewee.Model, Base):
	def __init__(self, env=None):
		super(PessoaContato,self).__init__()
		if env:
			database = env.db.connect()

	email               	= peewee.CharField(null=True)
	fax    	         	= peewee.CharField(null=True)
	celular             	= peewee.CharField(null=True)
	telefone            	= peewee.CharField(null=True)
	nome                	= peewee.CharField(null=True)
	telefone_empresarial	= peewee.CharField(null=True)
	skype				= peewee.CharField(null=True)
	observacoes			= peewee.CharField(null=True)
	data_cad           	= peewee.DateField(null=True)
	codigo				= peewee.BigIntegerField(null=True)
	pessoa				= peewee.BigIntegerField(null=True)
	padrao				= peewee.IntegerField(null=True)
	ativo				= peewee.IntegerField(null=True)

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
		db_table = 'pessoa_contato'

try:
	if database:
		database.evolve()
except peewee.OperationalError:
	PessoaContato.create_table()