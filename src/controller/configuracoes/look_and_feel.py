import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtCore import *
from src.view.configuracoes.look_and_feel import LookView

from src.controller.base import Base
from src.controller.widgets.buttons_cc import ButtonsCCController

from src.model.look import Look

class LookController(Base):
	def __init__(self, parent=None, env=None, force_show=False):
		super(Base, self).__init__()
		self.parent = parent
		self.view = LookView()
		self.model = Look()
		
		self.ctrlButtonsCC = ButtonsCCController()

		self.style = {
						'Defaut': '"background-color: ;" "color: ;"',
						'Light': '"background-color: rgb(255, 255, 255);" "color: rgb(102, 102, 102);"',
						'Dark':  '"background-color: rgb(102, 102, 102);" "color: rgb(255, 255, 255);"',
					 }

		self.fill_look()
		self.fill_style()

		self.dict = self.model.get_dict()
		self.view.set_ui(self.dict)

		#self.set_look()

		self.ctrlButtonsCC.view.bt_confirmar.clicked.connect(self.on_bt_confirmar)
		self.view.horizontalLayout.addWidget(self.ctrlButtonsCC.show())

		if force_show:
			self.view.show()

	def show(self):
		return self.view

	def fill_look(self):
		for estilo in QStyleFactory.keys():
			self.view.look_and_feel.addItem(estilo)

	def on_bt_confirmar(self):
		self.save_values()
		self.set_look()
		
	def fill_style(self):
		for style in self.style.keys():
			self.view.style_sheet.addItem(style)

	def save_values(self):
		self.dict = self.model.get_dict()
		dict = self.view.get_ui_dict()
		self.dict.update(dict)
		self.model.save_dict(self.dict)

	def set_look(self):
		dict = self.model.get_dict()
		if dict:
			look = self.view.look_and_feel.itemText(dict['look_and_feel'])
			QApplication.setStyle(QStyleFactory.create(look))
			
			style = self.view.style_sheet.itemText(dict['style_sheet'])

			self.view.setStyleSheet(eval(self.style[style]))
			
			if self.parent:
				self.parent.view.setStyleSheet(eval(self.style[style]))
			
			return style, eval(self.style[style])
			
	def saquetta(self):
		print(10)
		self.ctrlButtonsCC.view.bt_confirmar.clicked.connect(self.on_bt_confirmar)
		self.ctrlButtonsCC.view.bt_cancelar.hide()
		

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = LookController(force_show=True)
	sys.exit(app.exec_())
