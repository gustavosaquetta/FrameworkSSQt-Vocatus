import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/widgets/ui/buttons_cch.ui')
from src.view.widgets.ui.buttons_cch import Ui_ButtonsCCH

class ButtonsCCHView(QWidget, Ui_ButtonsCCH, SSQt):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		print('V botoes')
		self.bt_confirmar.clicked.connect(self.teste)
		self.bt_cancelar.clicked.connect(self.teste)

	def teste(self):
		print(0)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = ButtonsCCHView()
	w.show()
	sys.exit(app.exec_())
