import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/cadastro/ui/pessoa_contato.ui')
from src.view.cadastro.ui.pessoa_contato import Ui_Contato

class ContatoView(QWidget, Ui_Contato, SSQt):
	def __init__(self):
		super(ContatoView, self).__init__()
		self.setupUi(self)
		self.ui()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = ContatoView()
	w.show()
	sys.exit(app.exec_())
