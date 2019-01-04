import platform, sys, os
sys.path.append(os.getcwd())

from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5 import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

from lib.ssqt import SSQt

'''
Eu sei to repetindo muito codigo
os icones nao sao do mesmo tamanho
e alem disso fica mais facil caso um dia, mesmo que improvavavel
queiramos mudar o comportamento basico de cada janela....
rue rue rue brbbrbrbrbr
'''

widgetForm, baseClass = uic.loadUiType("sources/dialog/ui/error.ui")
class SSQtDialogError(widgetForm, baseClass):
	def __init__(self, msg=None):
		QDialog.__init__(self)
		self.setupUi(self)

		if not msg:
			msg = '<b>Não foi possível realizar a operação!</b><br>\nInforme o campo xnxx para prosseguir.'

		pixmap = QtGui.QPixmap('assets/images/dialog/error.png')
		self.img.setPixmap(pixmap)

		self.msg.setText(msg)
		
		#Eventos de botões
		self.bt_confirmar.clicked.connect(self.on_bt_confirmar)

	def main(self):
		app = QApplication(sys.argv)
		myWindow = SSQtDialogError()
		myWindow.show()
		app.exec_()
		
	def on_bt_confirmar(self):
		self.close()

		
widgetForm, baseClass = uic.loadUiType("sources/dialog/ui/info.ui")
class SSQtDialogInfo(widgetForm, baseClass):
	def __init__(self, msg=None):
		QDialog.__init__(self)
		self.setupUi(self)

		if not msg:
			msg = '<b>Não foi possível realizar a operação!</b><br>\nInforme o campo xnxx para prosseguir.'

		pixmap = QtGui.QPixmap('assets/images/dialog/info.png')
		self.img.setPixmap(pixmap)

		self.msg.setText(msg)
		
		#Eventos de botões
		self.bt_confirmar.clicked.connect(self.on_bt_confirmar)

	def main(self):
		app = QApplication(sys.argv)
		myWindow = SSQtDialogInfo()
		myWindow.show()
		app.exec_()
		
	def on_bt_confirmar(self):
		self.close()

widgetForm, baseClass = uic.loadUiType("sources/dialog/ui/alert.ui")
class SSQtDialogAlert(widgetForm, baseClass):
	def __init__(self, msg=None):
		QDialog.__init__(self)
		self.setupUi(self)

		if not msg:
			msg = '<b>Não foi possível realizar a operação!</b><br>\nInforme o campo xnxx para prosseguir.'

		pixmap = QtGui.QPixmap('assets/images/dialog/alert.png')
		self.img.setPixmap(pixmap)

		self.msg.setText(msg)
		
		#Eventos de botões
		self.bt_confirmar.clicked.connect(self.on_bt_confirmar)

	def main(self):
		app = QApplication(sys.argv)
		myWindow = SSQtDialogAlert()
		myWindow.show()
		app.exec_()
		
	def on_bt_confirmar(self):
		self.close()


widgetForm, baseClass = uic.loadUiType("sources/dialog/ui/question.ui")
class SSQtDialogQuestion(widgetForm, baseClass):
	def __init__(self, msg=None):
		QDialog.__init__(self)
		self.setupUi(self)

		if not msg:
			msg = '<b>Não foi possível realizar a operação!</b><br>\nTem certeza que deseja continuar.'

		pixmap = QtGui.QPixmap('assets/images/dialog/question.png')
		self.img.setPixmap(pixmap)
		self.msg.setText(msg)

		self.ret = None
		
		#Eventos de botões
		self.bt_confirmar.clicked.connect(self.on_bt_confirmar)
		self.bt_cancelar.clicked.connect(self.on_bt_cancelar)

	def main(self):
		app = QApplication(sys.argv)
		myWindow = SSQtDialogQuestion()
		myWindow.show()
		app.exec_()
		
	def on_bt_confirmar(self):
		self.ret = True
		print(self.ret)
		self.close()
		
	def on_bt_cancelar(self):
		self.ret = False
		print(self.ret)
		self.close()


widgetForm, baseClass = uic.loadUiType("sources/dialog/ui/find.ui")
class SSQtDialogFind(widgetForm, baseClass, SSQt):
	def __init__(self, tv_find_list=None, cb_campo_list=None, classe=None):
		QDialog.__init__(self)
		self.setupUi(self)

		self.classe = classe
		self.ret = None

		# Elementos do filtro
		self.cb_campo_list = cb_campo_list
		if not cb_campo_list:
			self.cb_campo_list = ["Nome", "Código"]

		self.cb_clausula_list = ["Iniciando com:", "Igual:", "Contém:"]
		
		self.cb_campo.addItems(self.cb_campo_list)
		self.cb_clausula.addItems(self.cb_clausula_list)

		#Eventos de botões
		self.bt_confirmar.clicked.connect(self.on_bt_confirmar)
		self.bt_cancelar.clicked.connect(self.on_bt_cancelar)

		self.tv_find_list = tv_find_list
		if not tv_find_list:
			self.tv_find_list = [('Código','codigo',100 ), 
								 ('Nome', 'nome', 200), 
								 ('all_form','all_form', 10)
								]

		# Inicializa o tree view
		self.tv_find_nome = self.tv_find.objectName()
		self.tv_find.setHeaderLabels([x[0] for x in self.tv_find_list])
		self.tv_find.setColumnCount(len(self.tv_find_list)-1)

		self.valor.textChanged.connect(self.fill_tree)
		self.limit.valueChanged.connect(self.fill_tree)

		if classe:
			self.fill_tree()

	def main(self):
		app = QApplication(sys.argv)
		myWindow = SSQtDialogFind()
		myWindow.show()
		app.exec_()


	def fill_tree(self):
		C = self.classe
		w = self.get_ui_dict()

		self.tv_find.clear()
		dict_list = C.get_data_finddialog(self, w)
		if dict_list:
			for dict in dict_list:
				self.insert_item_tree(self.tv_find_nome, self.tv_find_list, dict)

	def on_bt_confirmar(self):
		self.ret = self.get_data_tree(self.tv_find_nome, self.tv_find_list)
		print(self.ret)
		import pdb;pdb.set_trace()

		self.ret = self.get_selected_row(self.tv_find_nome, self.tv_find_list)
		print(self.ret)
		#self.close()

	def on_bt_cancelar(self):
		self.ret = False
		self.close()
		
if __name__ == "__main__":
	appcl = QApplication(sys.argv)
	w = DialogInfo()
	w.main()
	sys.exit(appcl.exec_())