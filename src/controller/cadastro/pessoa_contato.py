import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication

from src.view.cadastro.pessoa_contato import ContatoView

from src.controller.base import Base
from src.controller.widgets.buttons_cc import ButtonsCCController


class PessoaContatoController(Base):
	def __init__(self, parent=None, env=None, data={}, force_show=False):
		super(Base, self).__init__()
		self.parent = parent
		self.env = env
		self.view = ContatoView()
		self.dict = data

		#self.view.cep.setInputMask('99999-999')
		#self.view.inscricao_estadual.setInputMask('999.999.999.999')
		
		self.ctrlButtons = ButtonsCCController()
		self.view.horizontalLayout.addWidget(self.ctrlButtons.show())
		
		if self.dict:
			self.view.set_ui(self.dict)
		
		# Sinais dos botões
		self.ctrlButtons.view.bt_confirmar.clicked.connect(self.on_bt_confirmar)
		self.ctrlButtons.view.bt_cancelar.clicked.connect(self.on_bt_cancelar)

		if force_show:
			self.view.show()

	def show(self):
		return self.view
	
	def on_bt_confirmar(self):
		dict = self.view.get_ui_dict()

		if self.dict:
			dict = self.dict
			dict.update(self.view.get_ui_dict())

		self.ret = dict
		self.view.close()
			
	def on_bt_cancelar(self):
		self.view.close()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = PessoaContatoController(force_show=True)
	sys.exit(app.exec_())