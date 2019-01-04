import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.controller.base import Base
from src.controller.singleview.singleviewapp import SingleViewAppController
from src.controller.update_db import run_evolve
from src.controller.environment import Environment

class MainController:

	def show(self):
		status_update = 'Não foi possível realizar a atualização do banco de dados!'
		if os.environ.get('compileDb'):
			if run_evolve():
				status_update = 'Atualização do banco realizada com sucesso!'
				self.log.info()
		
		return SingleViewAppController(Environment(), True)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = MainController()
	sys.exit(app.exec_())
