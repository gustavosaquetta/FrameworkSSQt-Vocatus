import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/singleview/ui/login.ui')
from src.view.singleview.ui.login import Ui_Login

class LoginView(QWidget, Ui_Login, SSQt):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = LoginView()
	w.show()
	sys.exit(app.exec_())
