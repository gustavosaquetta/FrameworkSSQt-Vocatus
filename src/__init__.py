import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication
from src.controller.main import MainController

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainController().show()
	sys.exit(app.exec_())