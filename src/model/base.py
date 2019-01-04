import os, sys
from src.controller.lib.ssqt import SSQt
sys.path.append(os.getcwd())

from src.controller.environment import DataBase

class Base(object):
	def get_dict(self, select='*', where=""):
		value = self._get_data(select, where)
		if value:
			return value[0]
		else:
			return {}
			
	def get_dict_list(self, select='*', where=""):
		value = self._get_data(select, where)
		return value

	def _get_data(self, select='*', where=""):
		classe = str(self.__class__).lower()
		fim    = classe.find("'>")
		ini    = classe.rfind(".")
		table  = self._meta.db_table

		if where:
			where = ' where '+where

		sql = "select %s from %s %s" % (select, table, where)

		ret_dict_list = self.raw(sql).dicts()
		dict_list = []
		for ret_dict in ret_dict_list:
			dict_list.append(ret_dict)
		print(dict_list)
		return dict_list or []

	def insert_dict(self, obj):
		dict_add = {}

		for k, v in obj.items():
			if k in dir(self):
				dict_add.update({k:v})

		self.insert(**dict_add).execute()

	def save_dict(self, obj):
		if str(type(obj)) == "<class 'dict'>":
			obj_list = [obj]
		else:
			obj_list = obj
			
		for obj in obj_list:
			dict_add = {}
			if not obj.get('id'):
				self._meta.auto_increment = False
	
			for k, v in obj.items():
				# A classe do peewee se bate com tipo de dados vazio '', então mudar para None
				if k in dir(self) and v not in (None, ''): 
					dict_add.update({k:v})
				if k in dir(self) and v in (None, ''):
					dict_add.update({k:None})
					

			if not obj.get('id'):
				dict_add['id'] = self.get_new_id()
			print('tentando salvar: ', obj, dict_add)

			#todo implementar uma validacao par atualizar somente se o dicionário tiver ao menos uma chave modificada com relacao ao banco
			
			#if not obj.get('id'):
			self.__dict__['_data'].update(dict_add)

			if not obj.get('id'):
				self.save(force_insert=True)
			else:
				self.save()
		
			if not obj.get('id'):
				self._meta.auto_increment = True
	
		return dict_add
		
	def delete_dict(self, obj):
		if obj.get('id'):
			self.id = obj['id']
		self.delete_instance()
		
	def get_new_id(self):
		DB = DataBase()
		conn = DB.connect(autocommit=True)
		sql = "select general_id(0, nextval('general_id_seq')::int4)"
		return conn.execute_sql(sql).fetchone()[0]