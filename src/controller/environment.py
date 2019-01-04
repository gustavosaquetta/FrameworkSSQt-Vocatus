import sys, os
sys.path.append(os.getcwd())

import peewee

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication

from src.controller.lib.log import log
from src.controller.lib.ssqt import SSQt
from src.controller.config import ConfigDB

class DataBase:
	psql_db = None
	def __init__(self):
		print('banco de dados:',  id(self))
		pass

	def connect(self, conn_dict={}, try_connect=True, autocommit=True):
		env = Environment()
		CDB  = ConfigDB(env)

		if not conn_dict:
			conn_dict = CDB.read().get('database')

		# Se o banco for SQLite
		''''
		if str(conn_dict['banco']) == '1':
			sqlite_db = peewee.SqliteDatabase("%s.db" % conn_dict['database'])
			if try_connect:
				try:
					sqlite_db.connect()
					sqlite_db.close()
					return sqlite_db
				except:
					sqlite_db.close()
					return False
		'''
		if str(conn_dict['banco']) == '0':
			psql_db = peewee.PostgresqlDatabase(
				conn_dict.get('dbname') or conn_dict.get('database'),
				user         = conn_dict['user'],
				password     = conn_dict['password'],
				host         = conn_dict['host'],
				port         = conn_dict['port'],
				autocommit   = autocommit, 
				autorollback = autocommit,
				)
			
			if try_connect:
				try:
					psql_db.connect()
				except:
					a = QApplication(sys.argv)
					msg = QMessageBox()
					msg.setIcon(QMessageBox.Information)
					msg.setWindowTitle("Informação")
					msg.setText("Não foi possível conectar com o banco de dados!\nPor favor verifique suas configurações de conexão.")
					sys.exit(msg.exec_())
			return psql_db

class Environment:
	def __init__(self):
		self.db = DataBase()
		self.log = log
		self.lib= SSQt()

		
if __name__=="__main__":
	DB = DataBase()
	DB.connect(try_connect=True)