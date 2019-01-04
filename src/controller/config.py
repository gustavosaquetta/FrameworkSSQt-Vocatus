import sys, os, configparser
sys.path.append(os.getcwd())

from src.controller.lib.log import log

class ConfigDB(log):
	def __init__(self, env):
		self.env = env
		self.config = configparser.ConfigParser()

	def start(self):
		r = self.read()
		#r = {'database': {'host': 'localhost', 'dbname': 'vocatus', 'port': '5432', 'user': 'postgres', 'password': 'postgres'}}
		self.write(r)

	def read(self):
		try:
			self.config.read('config.ini')
			section_list = self.config.sections()
			dict_config = self.section_to_dict(section_list)

			if not dict_config:
				self.create()

			#self.log.info('Configurações do banco de dados carregadas com sucesso!')
			return dict_config
		except:
			#self.log.error('Não foi possível abrir o arquivo, tente novamente.')
			self.create()

	def create(self):
		self.config.add_section('database')
		self.config.set('database', 'base', '')
		self.config.set('database', 'host', '')
		self.config.set('database', 'dbname', '')
		self.config.set('database', 'port', '')
		self.config.set('database', 'user', '')
		self.config.set('database', 'password', '')
		self.config.set('database', 'banco', '1')

		with open('config.ini', 'w') as configfile:
			self.config.write(configfile)

	def section_to_dict(self, section):
		dict_options = {}
		dict_section = {}
		for section in section:
			options = self.config.options(section)
			for option in options:
				try:
					dict_options[option] = self.config.get(section, option)
					
					if dict_options[option] == -1:
						self.log.info("valor inválido para a sessão: %s - opção: %s" % (section, option))
				except:
					self.log.info("Chave inválida: %s!" % option)
					dict_options[option] = None

			dict_section[section] = dict_options
		return dict_section

	def write(self, dict):
		#to do validar se no dicionário tem campos novos que não estão no arquivo atual...
		for k, vdict in dict.items():

			if not self.config.has_section(k):
				self.config.add_section(k)

			for kd, vd in vdict.items():
				self.config.set(k, kd, vd)

		with open('config.ini', 'w') as configfile:
			self.config.write(configfile)
			self.log.info('Configurações do banco de dados salvas com sucesso!')

if __name__ == "__main__":
	C = ConfigDB()
	C.start()