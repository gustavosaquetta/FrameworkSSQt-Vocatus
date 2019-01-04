import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/configuracoes/ui/database.ui')
from src.view.configuracoes.ui.database import Ui_Database

class DatabaseView(QWidget, Ui_Database, SSQt):
	def __init__(self):
		super(DatabaseView, self).__init__()
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = DatabaseView()
	w.show()
	sys.exit(app.exec_())
