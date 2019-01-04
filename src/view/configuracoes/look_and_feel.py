import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/configuracoes.ui/look_and_feel.ui')
from src.view.configuracoes.ui.look_and_feel import Ui_Look

class LookView(QWidget, Ui_Look, SSQt):
	def __init__(self):
		super(LookView, self).__init__()
		self.setupUi(self)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = LookView()
	w.show()
	sys.exit(app.exec_())
