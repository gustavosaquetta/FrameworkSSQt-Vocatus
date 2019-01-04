'''
Created on 29 de out de 2017

@author: gustavosaquetta
'''

import sys, os
sys.path.append(os.getcwd())
from PyQt5.Qt import QApplication
from src.controller.lib.ssqt import SSQt

from src.controller.finder.finder import FinderController
from src.controller.cadastro.pessoa import PessoaController

class FinderPessoa(FinderController):

	def __init__(self, parent=None, env=None, feedClass=None, tv_find_list=None, cb_campo_list=None, force_show=None):
		
		campos = ['Nome', 'Código']
		super(FinderPessoa, self).__init__(parent=parent, env=env, feedClass=PessoaController, tv_find_list=tv_find_list, cb_campo_list=cb_campo_list, force_show=force_show)
		self.view.setWindowTitle('Localizar Cliente')


if __name__ == "__main__":
	appcl = QApplication(sys.argv)
	w = FinderPessoa(force_show=True)
	sys.exit(appcl.exec_())