import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/widgets/ui/buttons_cc.ui')
from src.view.widgets.ui.buttons_cc import Ui_ButtonsCC

class ButtonsCCView(QWidget, Ui_ButtonsCC, SSQt):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		#self.bt_cancelar.hide()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = ButtonsCCView()
	w.show()
	sys.exit(app.exec_())
