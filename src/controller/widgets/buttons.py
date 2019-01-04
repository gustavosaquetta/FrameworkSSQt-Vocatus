import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.view.widgets.buttons import ButtonsView
from src.controller.base import Base

class ButtonsController(Base):
	def __init__(self, force_show=False):
		self.view = ButtonsView()

		if force_show:
			self.view.show()

	def show(self):
		return self.view

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = ButtonsController(True).show()
	sys.exit(app.exec_())
