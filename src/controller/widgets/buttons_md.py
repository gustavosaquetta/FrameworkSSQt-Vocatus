import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.view.widgets.buttons_md import ButtonsMDView
from src.controller.base import Base

class ButtonsMDController:
	def __init__(self, force_show=False):
		print('MD botoes')
		self.view = ButtonsMDView()

		self.view.bt_add.clicked.connect(self.on_bt_confirmare)
		
		if force_show:
			self.view.show()

	def show(self):
		return self.view

	def on_bt_confirmare(self):
		print(10)

	def validate_user(self):
		if True:
			self.auth = True

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = ButtonsMDController(True)
	sys.exit(app.exec_())
