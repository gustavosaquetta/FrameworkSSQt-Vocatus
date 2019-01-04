import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QDialog

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/widgets/ui/buttons.ui')
from src.view.widgets.ui.buttons import Ui_Buttons

class ButtonsView(QDialog, Ui_Buttons, SSQt):
	def __init__(self):
		super(ButtonsView, self).__init__()
		self.setupUi(self)
		self.bt_ajuda.hide()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = ButtonsView()
	w.show()
	sys.exit(app.exec_())
