import os, sys
sys.path.append(os.getcwd())

import peewee as peewee

from src.controller.lib.ssevolutive import *
from src.controller.environment import Environment


from src.model.sequences import *
from src.model.functions import *

from src.model.config import *
from src.model.cliente import *
from src.model.cadastro.empresa import *

def run_evolve():
	#Atualiza o banco de dados se necessário
	env = Environment()
	db = env.db.connect()
	if db:
		try:
			db.evolve()
		except:
			pass
