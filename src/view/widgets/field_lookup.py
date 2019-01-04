import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/widgets/ui/field_lookup.ui')
from src.view.widgets.ui.field_lookup import Ui_FieldLookup

class FieldLookupView(QWidget, Ui_FieldLookup, SSQt):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		print('FieldLookup')

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = FieldLookupView()
	w.show()
	sys.exit(app.exec_())
