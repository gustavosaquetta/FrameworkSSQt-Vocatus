'''
Created on 29 de out de 2017

@author: gustavosaquetta
'''

from src.model.cadastro.pessoa import Pessoa
from src.controller.lib.ssqt import SSQt

class PessoaController:
	
	
	def formata_cpf_cnpj(self, view):
		if view:
			#SSQt().pdb()
			if hasattr(view, 'tipo_1'):
				if view.tipo_1.isChecked():
					view.cpf.setInputMask('999.999.99-99')
	
				if view.tipo_2.isChecked():
					view.cpf.setInputMask('99.999.999/9999-99')

			if view.cpf.text():
				if not Cpf(view.cpf.text()).validate():
					view.cpf.setText('')


	def get_data_finderdialog(self, filtro=None):
		C = Pessoa
		campo    = None 
		clausula = None
		if filtro and filtro.get('valor'):
			if filtro.get('cb_campo') == 0:
				campo = 'nome'
			elif filtro.get('cb_campo') == 1:
				campo = 'codigo'
			
			if filtro.get('cb_clausula') == 0:
				clausula = 'ilike'
				filtro['valor'] = filtro['valor']+'%%'
			elif filtro.get('cb_clausula') == 1:
				clausula = '=='
			elif filtro.get('cb_clausula')==2:
				clausula = 'ilike'
				filtro['valor'] = '%%'+filtro['valor']+'%%'
			
			if campo and clausula:
				sql = "select * from pessoa where %s::text %s '%s' order by codigo limit %s" % (campo, clausula, filtro['valor'], filtro['limit'])
				return C.raw(sql).dicts()

			elif filtro.get('valor'):
				sql = "select * from pessoa where %s::text %s '%s' limit 1" % (filtro['campo'], filtro['clausula'], filtro['valor'])
				return C.raw(sql).dicts()

	
		return C.select().dicts()
	
class Cnpj(object):

	def __init__(self, cnpj):
		"""
		Class to interact with cnpj brazilian numbers
		"""
		self.cnpj = cnpj

	def calculating_digit(self, result):
		result = result % 11
		if result < 2:
			digit = 0
		else:
			digit = 11 - result
		return str(digit)

	def calculating_first_digit(self):
		one_validation_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4 , 3, 2]
		result = 0
		pos = 0
		for number in self.cnpj:
			try:
				one_validation_list[pos]
			except IndexError:
				break
			result += int(number) * int(one_validation_list[pos])
			pos += 1
		return self.calculating_digit(result)

	def calculating_second_digit(self):
		two_validation_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
		result = 0
		pos = 0
		for number in self.cnpj:
			try:
				two_validation_list[pos]
			except IndexError:
				break
			result += int(number) * int(two_validation_list[pos])
			pos += 1
		return self.calculating_digit(result)

	def validate(self):
		"""
		Method to validate brazilian cnpjs
		"""
		self.cnpj = self.cleaning()

		if len(self.cnpj) != 14:
			return False

		checkers = self.cnpj[-2:]

		digit_one = self.calculating_first_digit()
		digit_two = self.calculating_second_digit()

		return bool(checkers == digit_one + digit_two)

	def cleaning(self):
		return self.cnpj.replace('-', '').replace('.', '').replace('/', '')

	def format(self):
		"""
		Method to format cnpj numbers.
		"""
		return '%s.%s.%s/%s-%s' % (self.cnpj[0:2], self.cnpj[2:5],
			self.cnpj[5:8], self.cnpj[8:12], self.cnpj[12:14])

class Cpf(object):

	def __init__(self, cpf):
		self.cpf = cpf

	def validate_size(self):
		cpf = self.cleaning()
		if len(cpf) > 11 or len(cpf) < 11:
			return False
		return True

	def validate(self):
		if self.validate_size():
			digit_1 = 0
			digit_2 = 0
			i = 0
			cpf = self.cleaning()
			while i < 10:
				digit_1 = ((digit_1 + (int(cpf[i]) * (11-i-1))) % 11
					if i < 9 else digit_1)
				digit_2 = (digit_2 + (int(cpf[i]) * (11-i))) % 11
				i += 1
			return ((int(cpf[9]) == (11 - digit_1 if digit_1 > 1 else 0)) and
					(int(cpf[10]) == (11 - digit_2 if digit_2 > 1 else 0)))
		return False

	def cleaning(self):
		return self.cpf.replace('.', '').replace('-', '')

	def format(self):
		return '%s.%s.%s-%s' % (
			self.cpf[0:3], self.cpf[3:6], self.cpf[6:9], self.cpf[9:11])