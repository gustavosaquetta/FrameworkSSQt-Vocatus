import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.view.cadastro.empresa import EmpresaView

from src.controller.base import Base
from src.controller.widgets.buttons import ButtonsController
from src.controller.widgets.buttons_md import ButtonsMDController
from src.controller.widgets.field_lookup import FieldLookupController
from src.controller.cadastro.pessoa import PessoaController

from src.model.cadastro.pessoa import Pessoa
from src.model.cadastro.pessoa_contato import PessoaContato

class EmpresaController(Base):
	def __init__(self, parent=None, env=None, force_show=False):
		super(Base, self).__init__()
		self.parent = parent
		self.env = env
		self.view = EmpresaView()
		self.model = Pessoa(self.env)
		self.model_contato = PessoaContato(self.env)
		self.dict = {}
		self.remove_contato_list = []
		
		self.view.cep.setInputMask('99999-999')
		self.view.inscricao_estadual.setInputMask('999.999.999.999')
		
		self.view.tipo_1.toggled.connect(lambda: PessoaController().formata_cpf_cnpj(self.view))
		self.view.tipo_2.toggled.connect(lambda: PessoaController().formata_cpf_cnpj(self.view))

		self.ctrlButtons = ButtonsController()
		self.view.horizontalLayout.addWidget(self.ctrlButtons.show())
		
		self.ctrlButtonsMD = ButtonsMDController()
		self.view.horizontalLayoutMasterDetalhe.addWidget(self.ctrlButtonsMD.show())
		
		#lookup grupo pessoa # meio grande mas por hora é p mdelo padrão		
		self.ctrlLookupGrupo = FieldLookupController(parent=self)
		self.view.verticalLayoutLookupGrupo.addWidget(self.ctrlLookupGrupo.show())
		self.ctrlLookupGrupo.pessoaGrupoLookup(self.view)
		old_value = self.view.pessoa_grupo_codigo.property('id')
		params_tuple = (self.parent, self.ctrlLookupGrupo, 'FinderPessoa(parent=None, env=None, feedClass=None, tv_find_list=None, cb_campo_list=None, force_show=None)', old_value)
		self.view.pessoa_grupo_codigo.editingFinished.connect(lambda: self.ctrlLookupGrupo.prepare_lookup(finder=params_tuple))
		self.view.pessoa_grupo_codigo.returnPressed.connect(lambda: self.ctrlLookupGrupo.prepare_lookup(finder=params_tuple, pressKey=True))

		#lookup municipio
		self.ctrlLookupMunicipio = FieldLookupController(parent=self)
		self.view.verticalLayoutLookupMunicipio.addWidget(self.ctrlLookupMunicipio.show())
		self.ctrlLookupMunicipio.municipioLookup(self.view)

		#lookup pais
		self.ctrlLookupPais = FieldLookupController(parent=self)
		self.view.verticalLayoutLookupPais.addWidget(self.ctrlLookupPais.show())
		self.ctrlLookupPais.paisLookup(self.view)
		
		#lookup cnae
		self.ctrlLookupCnae = FieldLookupController()
		self.view.verticalLayoutLookupCnae.addWidget(self.ctrlLookupCnae.show())
		self.ctrlLookupCnae.cnaeLookup(self.view)
		
		#Tabela de contato
		self.tv_contato = self.view.tv_contato
		self.tv_contato = [('Código','codigo',100 ), 
							 ('Nome', 'nome', 110),
							 ('Celular', 'celular', 110),
							 ('E-mail', 'email', 200),
							 ('all_form','all_form', 10)
							]
	
		# Inicializa o tree view
		self.tv_contato_nome = self.view.tv_contato.objectName()
		self.view.tv_contato.setHeaderLabels([x[0] for x in self.tv_contato])
		self.view.tv_contato.setColumnCount(len(self.tv_contato)-1)
		
		# Sinais dos botões
		self.ctrlButtons.view.bt_salvar.clicked.connect(self.on_bt_confirmar)
		self.ctrlButtons.view.bt_pesquisar.clicked.connect(self.on_bt_pesquisar)
		self.ctrlButtons.view.bt_novo.clicked.connect(self.on_bt_novo)
		self.ctrlButtons.view.bt_apagar.clicked.connect(self.on_bt_apagar)
		
		self.ctrlButtonsMD.view.bt_add.clicked.connect(self.on_bt_add_contato)
		self.ctrlButtonsMD.view.bt_edit.clicked.connect(self.on_bt_edit_contato)
		self.ctrlButtonsMD.view.bt_del.clicked.connect(self.on_bt_del_contato)
		#self.parent.view.setEnabled(False)
		if force_show:
			self.view.show()

	def show(self):
		return self.view
	
	def on_bt_confirmar(self):
		empresa_dict = self.view.get_ui_dict()
		contato_dict_list = self.view.get_data_tree(self.tv_contato_nome, self.tv_contato)

		if self.dict:
			empresa_dict = self.dict
			empresa_dict.update(self.view.get_ui_dict())

		try:
			self.model.begin()
			
			if contato_dict_list:
				self.model_contato.begin()
			
			self.dict = self.model.save_dict(empresa_dict)

			if contato_dict_list:
				for contato_dict in contato_dict_list:
					contato_dict['pessoa'] = self.dict['id']
					self.model_contato.save_dict(contato_dict)

			self.model.commit()

			if self.remove_contato_list:
				for contato in self.remove_contato_list:
					self.model_contato.delete_dict(contato)

			if contato_dict_list:
				self.model_contato.commit()

		except:
			self.model.rollback()
			
			if contato_dict_list:
				self.model_contato.rollback()
			
			self.parent.onPopupDialog(text='Não foi possível salvar!', type='error')

		if self.parent:
			self.parent.onPopupDialog(text='Empresa salva com sucesso!', type='info')

	def fill_tv_contato(self):
		self.view.tv_contato.clear()
		if self.dict:
			contato_dict_list = self.model_contato.get_dict_list(where='pessoa=%d' % self.dict['id'])

		if contato_dict_list:
			for contato_dict in contato_dict_list:
				self.view.insert_item_tree(self.tv_contato_nome, self.tv_contato, contato_dict)

		v = self.view.get_data_tree(self.tv_contato_nome, self.tv_contato)

	def on_bt_pesquisar(self):
		if self.parent:
			self.parent.onpopUpFrame(frame='FinderPessoa()')
			empresa_dict = self.wait_return(self.parent)

			if empresa_dict:
				self.dict = empresa_dict
				self.view.set_ui(empresa_dict)

				self.fill_tv_contato()

	def on_bt_novo(self):
		self.dict = {}
		self.view.clrscr()
		self.view.tv_contato.clear()

	def on_bt_apagar(self):
		self.model.delete_dict(self.dict)
		self.on_bt_novo()
		self.parent.onPopupDialog(text='Empresa removida com sucesso!', type='info')

	def on_bt_add_contato(self):
		self.parent.onpopUpFrame(frame='PessoaContatoController()')
		contato_dict = self.wait_return(self.parent)

		if contato_dict:
			contato_dict['pessoa'] = self.dict.get('id')

		if contato_dict:
			self.view.insert_item_tree(self.tv_contato_nome, self.tv_contato, contato_dict)

	def on_bt_edit_contato(self):
		contato_dict = self.view.get_selected_row(self.tv_contato_nome, self.tv_contato)
		if not contato_dict:
			self.parent.onPopupDialog(text='Não foi possível realizar a edição!\nSelecione um contato para prosseguir.', type='alert')
			return

		self.parent.onpopUpFrame(frame='PessoaContatoController(data=self.data)', data=contato_dict)
		contato_dict = self.wait_return(self.parent)

		if contato_dict:
			self.view.alter_item_tree(self.tv_contato_nome, self.tv_contato, contato_dict)
		
	def on_bt_del_contato(self):
		self.view.remove_item_tree(self.tv_contato_nome)
		contato_db_list = self.model_contato.get_dict_list(where='pessoa=%d' % self.dict['id'])
		contato_tv_list = self.view.get_data_tree(self.tv_contato_nome, self.tv_contato)
		#self.view.pdb()
		
		id_tv_list = [x['id'] for x in contato_tv_list if x.get('id') ]
		self.remove_contato_list = [x for x in contato_db_list if x['id'] not in id_tv_list]


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = EmpresaController(force_show=True)
	sys.exit(app.exec_())