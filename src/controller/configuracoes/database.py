import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.view.configuracoes.database import DatabaseView
from src.controller.base import Base
from src.controller.widgets.buttons_cc import ButtonsCCController

class DatabaseController(Base):
	def __init__(self, parent=None, env=None, force_show=False):
		super(Base, self).__init__()
		self.parent = parent
		self.env = env
		self.view = DatabaseView()

		if force_show:
			self.view.show()

		self.crtlButtonsCC = ButtonsCCController()
		self.view.horizontalLayout.addWidget(self.crtlButtonsCC.show())

	def show(self):
		return self.view

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = DatabaseController(True)
	sys.exit(app.exec_())
