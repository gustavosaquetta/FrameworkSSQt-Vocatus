import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.view.widgets.field_lookup import FieldLookupView
from src.controller.base import Base
from src.controller.finder.finder_pessoa import FinderPessoa

class FieldLookupController(Base):
	def __init__(self, parent=None, force_show=False, nome='lookup'):
		print('MD botoes')
		self.view = FieldLookupView()
		self.parent = parent

		if force_show:
			self.view.show()

	def show(self):
		return self.view
	
	def pessoaGrupoLookup(self, view):
		setattr(view, 'pessoa_grupo_codigo', self.view.lineEditLookup)
		setattr(view, 'pessoa_grupo', self.view.groupBoxLookup)
		setattr(view, 'pessoa_grupo.whatsThis', 'lookup_grupo_pessoa')

		# ToDo sql necessário....

	def municipioLookup(self, view):
		setattr(view, 'municipio_codigo', self.view.lineEditLookup)
		setattr(view, 'municipio', self.view.groupBoxLookup)
		setattr(view, 'municipio.whatsThis', 'lookup_municipio')

		# ToDo sql necessário....
		
	def paisLookup(self, view):
		setattr(view, 'pais_codigo', self.view.lineEditLookup)
		setattr(view, 'pais', self.view.groupBoxLookup)
		setattr(view, 'pais.whatsThis', 'lookup_pais')

		# ToDo sql necessário....
		
	def cnaeLookup(self, view):
		setattr(view, 'cnae_codigo', self.view.lineEditLookup)
		setattr(view, 'cnae', self.view.groupBoxLookup)
		setattr(view, 'cnae.whatsThis', 'lookup_cnae')

	def update_lookup(self, finder=None, pressKey=False):
		# Simples demais para as metas para fazer algo tão obsoleto!
		# Simplesmente forão muitos dias os que ue contei 16/10/17 a 01/11/17
		#self.FC = FinderPessoa(self)
		#va= self.FC.execute()
		
		if not self.view.lineEditLookup.text() and self.view.groupBoxLookup.title():
			self.view.groupBoxLookup.setTitle('')
			self.view.groupBoxLookup.setProperty('id', '')
			#dd = {
			#	'groupBoxLookup': None, 
			#	'groupBoxLookup_title': '', 
			#	'lineEditLookup': '',
			#}
			#self.view.set_ui(dd)
		
		parent    = finder[0]
		lookup    = finder[1]
		frame     = finder[2]
		old_value = finder[3]
		dict = {}
		if hasattr(self.view.lineEditLookup, 'text'):
			value = self.view.lineEditLookup.text()
		if hasattr(self.view.lineEditLookup, 'value'):
			value = self.view.lineEditLookup.value()
		if value:
			dict = {'valor':value, 'campo':'codigo', 'clausula':'='}

		value_id = self.view.groupBoxLookup.property('id')
		if (not dict and value_id) or (old_value and old_value!=value_id):
			dict = {'valor':value_id, 'campo':'id', 'clausula':'='}

		FC = eval(frame)
		FCC = FC.feedClass()
		ret = FCC.get_data_finderdialog(dict)

		d = {}
		if ret and value or value_id:
			for dict in ret:
				if dict.get('id') and dict.get('nome', 'descricao') and dict.get('codigo', 'numero'):
					d = {
							'groupBoxLookup': dict.get('id', 'grid'), 
							'groupBoxLookup_title': '   ' + dict.get('nome', 'descricao'),
							'lineEditLookup': str(dict.get('codigo', 'numero')),
						}

		# Se foi pressionado Enter
		if pressKey:
			if parent:
				parent.onpopUpFrame(frame='FinderPessoa()')
				ret_pop = self.wait_return(parent)

				if ret_pop and ret_pop.get('id') and ret_pop.get('nome', 'descricao') and ret_pop.get('codigo', 'numero'):
					d = {
							'groupBoxLookup': ret_pop.get('id', 'grid'), 
							'groupBoxLookup_title': '   ' + ret_pop.get('nome', 'descricao'), 
							'lineEditLookup': str(ret_pop.get('codigo', 'numero')),
						}

		if d:
			self.view.set_ui(d)
		else:
			self.view.clrscr()
		
		
	def prepare_lookup(self, finder=None, pressKey=None):
		self.update_lookup(finder=finder, pressKey=pressKey)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = FieldLookupController(True)
	sys.exit(app.exec_())
