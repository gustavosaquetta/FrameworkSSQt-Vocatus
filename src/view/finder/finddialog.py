import platform, sys, os
sys.path.append(os.getcwd())

from PyQt5 import uic
from PyQt5.QtWidgets import * 
from PyQt5 import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *

from sources.dialog.dialog import SSQtDialogFind

class DialogFindCliente(SSQtDialogFind):

	def __init__(self, *args, **kwargs):
		from controller.cliente import ClienteController
		campos = ['Nome', 'Código']
		super(DialogFindCliente, self).__init__(cb_campo_list=campos, classe=ClienteController)
		self.setWindowTitle('Localizar Cliente')

	def main(self):
		app = QApplication(sys.argv)
		myWindow = DialogFindCliente()
		myWindow.show()
		app.exec_()

	def on_bt_confirmar(self):
		self.ret = self.get_selected_row(self.tv_find_nome, self.tv_find_list)
		print(self.ret)
		self.pdb()
		self.close()	
		
if __name__ == "__main__":
	appcl = QApplication(sys.argv)
	w = DialogFindCliente()
	w.main()
	sys.exit(appcl.exec_())