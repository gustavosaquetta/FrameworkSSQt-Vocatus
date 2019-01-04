import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/widgets/ui/buttons_md.ui')
from src.view.widgets.ui.buttons_md import Ui_ButtonsMD

class ButtonsMDView(QWidget, Ui_ButtonsMD, SSQt):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		print('V botoes')
		self.bt_add.clicked.connect(self.teste)
		self.bt_edit.clicked.connect(self.teste)
		self.bt_del.clicked.connect(self.teste)

	def teste(self):
		print(0)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = ButtonsMDView()
	w.show()
	sys.exit(app.exec_())
