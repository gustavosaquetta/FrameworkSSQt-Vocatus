import platform, sys, os
sys.path.append(os.getcwd())

from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5 import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

from sources.dialog.finddialog import DialogFindCliente


def lookup_cliente(parent):
	LC = LookupCliente(parent)
	LC.exec_()

class LookupCliente(DialogFindCliente):

	def __init__(self, parent):
		from controller.cliente import ClienteController
		campos = ['Nome', 'Código']
		super(LookupCliente, self).__init__(cb_campo_list=campos, classe=ClienteController)
		self.setWindowTitle('Localizar Cliente')

		self.parent = parent

	def prepare_view(self, parent):
		parent.grupo.setProperty('id', int(self.ret.get('id')))
		parent.grupo.setProperty('title', self.ret.get('nome'))
		parent.grupo_codigo.setProperty('text', self.ret.get('codigo'))

if __name__ == "__main__":
	appcl = QApplication(sys.argv)
	w = LookupCliente()
	w.main()
	sys.exit(appcl.exec_())