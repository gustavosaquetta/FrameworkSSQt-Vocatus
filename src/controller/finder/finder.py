'''
Created on 29 de out de 2017

@author: gustavosaquetta
'''
import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.view.finder.finder import FinderView

from src.controller.base import Base
from src.controller.widgets.buttons_cch import ButtonsCCHController


class FinderController(Base):
	def __init__(self, parent=None, env=None, feedClass=None, tv_find_list=None, cb_campo_list=None, force_show=False):
		super(Base, self).__init__()
		self.parent = parent
		self.env = env
		self.view = FinderView()

		self.ctrlButtons = ButtonsCCHController()

		self.view.verticalLayoutButtonsCCH.addWidget(self.ctrlButtons.show())
		
		if force_show:
			self.view.show()

		self.feedClass = feedClass
		self.ret = None
	
		# Elementos do filtro
		self.cb_campo_list = cb_campo_list
		if not cb_campo_list:
			self.cb_campo_list = ["Nome", "Código"]
	
		self.cb_clausula_list = ["Iniciando com:", "Igual:", "Contém:"]
		
		self.view.cb_campo.addItems(self.cb_campo_list)
		self.view.cb_clausula.addItems(self.cb_clausula_list)
	
		#Eventos de botões
		self.ctrlButtons.view.bt_confirmar.clicked.connect(self.on_bt_confirmar)
		self.ctrlButtons.view.bt_cancelar.clicked.connect(self.on_bt_cancelar)
	
		self.tv_find_list = tv_find_list
		if not tv_find_list:
			self.tv_find_list = [('Código','codigo',100 ), 
								 ('Nome', 'nome', 200), 
								 ('all_form','all_form', 10)
								]
	
		# Inicializa o tree view
		self.tv_find_nome = self.view.tv_find.objectName()
		self.view.tv_find.setHeaderLabels([x[0] for x in self.tv_find_list])
		self.view.tv_find.setColumnCount(len(self.tv_find_list)-1)
	
		self.view.valor.textChanged.connect(self.fill_tree)
		self.view.limit.valueChanged.connect(self.fill_tree)
	
		if self.feedClass:
			self.fill_tree()

		return self.ret

	def show(self):
		return self.view
		
	def execute(self):
		'''
		app = QApplication(sys.argv)
		myWindow = self.view
		myWindow.show()
		app.exec_()
		'''
		return self.view.exec_()

	def fill_tree(self):
		C = self.feedClass
		w = self.view.get_ui_dict()

		self.view.tv_find.clear()
		dict_list = C.get_data_finderdialog(self, w)

		if dict_list:
			for dict in dict_list:
				self.view.insert_item_tree(self.tv_find_nome, self.tv_find_list, dict)

	def on_bt_confirmar(self):
		#self.ret = self.view.get_data_tree(self.tv_find_nome, self.tv_find_list)
		#self.ret = self.get_row_data()
		self.ret = self.view.get_selected_row(self.tv_find_nome, self.tv_find_list)
		print('confirmou dialog ', self.ret)
		self.view.close()

	def get_row_data(self):
		self.ret = self.view.get_selected_row(self.tv_find_nome, self.tv_find_list)

	def on_bt_cancelar(self):
		self.ret = False
		self.view.close()
		
if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = FinderController(force_show=True)
	sys.exit(app.exec_())