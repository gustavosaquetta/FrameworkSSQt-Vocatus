import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget, QDialog

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/finder/ui/finder.ui')
from src.view.finder.ui.finder import Ui_Finder

class FinderView(QWidget, Ui_Finder, SSQt):
	def __init__(self):
		super(FinderView, self).__init__()
		self.setupUi(self)
		self.ui()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = FinderView()
	w.show()
	sys.exit(app.exec_())