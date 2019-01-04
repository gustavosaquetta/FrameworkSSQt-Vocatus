import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.view.singleview.login import LoginView
from src.controller.base import Base

class LoginController(Base):
	def __init__(self, force_show=False):

		self.view = LoginView()
		self.auth = False

		if force_show:
			self.view.show()

		self.view.bt_login.clicked.connect(self.on_bt_login)

	def show(self):
		return self.view

	def on_bt_login(self):
		print('Login Controller')
		win_dict = self.view.get_ui_dict()
		if not win_dict['user'] and not win_dict['password']:
			self.validate_user()

	def validate_user(self):
		if True:
			self.auth = True


if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = LoginController(True)
	sys.exit(app.exec_())
