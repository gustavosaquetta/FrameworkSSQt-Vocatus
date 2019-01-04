import os, sys
from src.controller.widgets.spinner import WaitingSpinner
from src.controller.lib.ssqt import SSQt
sys.path.append(os.getcwd())

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt

from src.controller.finder.finder import FinderController
from src.controller.finder.finder_pessoa import FinderPessoa
from src.controller.cadastro.pessoa_contato import PessoaContatoController
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel

class PopUpWidget(QtWidgets.QWidget):
	def __init__(self, parent=None,  text='', type=None, frame=None, data=None):
		super(PopUpWidget, self).__init__(parent=parent)
		#self.setupUi(self)
		
		# faz o frame diferente
		#self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		#self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
		
		#propriedades do frame
		self.fillColor = QtGui.QColor(30, 30, 30, 120)
		self.penColor = QtGui.QColor("#333333")

		self.popup_fillColor = QtGui.QColor(255, 255, 255, 255)
		self.popup_penColor = QtGui.QColor(200, 200, 200, 255)

		self.popup_width = 500
		self.popup_height = 200
		
		#Atributos da classe
		self.image = None
		self.classe = None
		self.retorno = None
		self.text = text or 'Omae wa mou shindeiru (default)!'
		self.frame = frame
		self.type = type
		self.data = data
		#self.frame = 'FinderPessoa(parent=None, env=None, feedClass=None, tv_find_list=None, cb_campo_list=None, force_show=None)'

		# objetos da classe
		self.bt_confirmar = QtWidgets.QPushButton(self)
		self.bt_confirmar.hide()
		self.bt_confirmar.clicked.connect(self.on_bt_confirmar)

		self.bt_cancelar = QtWidgets.QPushButton(self)
		self.bt_cancelar.hide()
		self.bt_cancelar.clicked.connect(self.on_bt_cancelar)
		
		self.bt_close = QtWidgets.QPushButton(self)
		self.bt_close.hide()
		self.bt_close.clicked.connect(self.on_bt_sair)
		
		#self.clicked.connect(self.on_bt_sair)
		
		self.inicialize()
		return self.retorno

	def inicialize(self, text='', frame=None, type=None, data=None):

		self.frame = frame
		self.type = type
		self.text = text
		self.bt_confirmar.hide()
		self.bt_cancelar.hide()
		self.bt_close.hide()
		self.spinner = None
		self.data = data

		if self.image:
			self.image.hide()
		
		if self.type == 'loading':
			self.spinner = WaitingSpinner(
										self,
										roundness=19.0, 
										opacity=15.0,
										fade=70.0, 
										radius=8.0, 
										lines=8,
										line_length=30.0, 
										line_width=8.0,
										speed=1.0, 
										color=(0, 170, 255)
									)
		else:
			if self.frame and not (self.text or self.type):
				# feito para exibir classes dentro do view
				self.classe = eval(self.frame)
				self.frame = self.classe.show()
				self.vbox = QHBoxLayout()
				self.setLayout(self.vbox)
				self.vbox.addWidget(self.frame)
				self.classe.ctrlButtons.view.bt_cancelar.clicked.connect(lambda: self.bt_cancelar.click())
				self.classe.ctrlButtons.view.bt_confirmar.clicked.connect(lambda: self.bt_confirmar.click())

			else:
				style = "QPushButton:hover {\n"\
												"background-color: rgb(255, 255, 255);\n"\
												"color: rgb(21, 151, 255);\n"\
												"border-color:  rgb(21, 151, 255);\n"\
												"border-style: solid;\n"\
												"border-width: 2px;\n"\
												"}\n"\
												"\n"\
												"QPushButton:pressed {\n"\
												" background-color: rgb(0, 99, 149)\n"\
												"}\n"\
												"\n"\
												"QPushButton:disabled {\n"\
												"	background-color: rgb(100, 100, 100)\n"\
												"}\n"\
												"\n"\
												"QPushButton{\n"\
												"background-color: rgb(0, 170, 255);\n"\
												"border-radius: 15px;\n"\
												"color: rgb(255, 255, 255);\n"\
												"font-weight: bold;\n"\
												"}\n"\
												""

				self.bt_close.show()
				self.bt_close.setText("X")
				font = QtGui.QFont()
				font.setPixelSize(18)
				font.setBold(True)
				self.bt_close.setFont(font)
				self.bt_close.setFixedSize(30, 30)
	
				self.bt_close.setGeometry(QtCore.QRect(10, 10, 30, 30))
				self.bt_close.setStyleSheet(style)
	
				self.bt_confirmar.show()
				self.bt_confirmar.setText("Confirmar")
				self.bt_confirmar.setObjectName("bt_confirmar")
				self.bt_confirmar.setGeometry(QtCore.QRect(10, 10, 100, 30))
				self.bt_confirmar.setStyleSheet(style)

			if self.type:
				self.image = QtWidgets.QLabel(self)
				self.image.setPixmap(QtGui.QPixmap("assets/images/%s.jpg" % self.type))
				self.image.show()

				if self.type == 'question':
					self.bt_cancelar.show()
					self.bt_cancelar.setText("Cancelar")
					self.bt_cancelar.setObjectName("bt_cancelar")
					self.bt_cancelar.setGeometry(QtCore.QRect(10, 10, 100, 30))
					self.bt_cancelar.setStyleSheet(style)
					
		self.position()

		#print(1)
		#self.retorno = None
		#self.SIGNALS = PopUpWidgetSignals()
		
	def on_bt_confirmar(self):
		self.retorno = True

		if self.classe:
			if hasattr(self.classe, 'self.classe.get_row_data()'):
				self.retorno = self.classe.get_row_data()

			self.retorno = self.classe.ret
			print('Confirmou o popup com o retorno. %r' % self.retorno)

		print('Confirmou o popup. %s' % self.type or self.classe)
		self.quit()

	def on_bt_cancelar(self):
		self.retorno = False
		print('Cancelou o popup. %s' % self.type or self.classe)
		self.quit()

	def on_bt_sair(self):
		self.retorno = False
		print('Saiu (X) do popup. %s' % self.type or self.classe)
		self.quit()

	def resizeEvent(self, event):
		self.position()

	def position(self):
	
		if not self.frame:
			s = self.size()
			x = int(s.width() / 2 - self.popup_width / 2)
			y = int(s.height() / 2 - self.popup_height / 2)

			if self.type == 'loading':
				self.spinner.move(x + 50, y+60)
				self.spinner.start()
			else:
				self.bt_close.move(x + 465, y + 5)
				self.bt_confirmar.move(x + 200, y + 150)
				if self.image:
					self.image.move(x + 20, y+60)

				if self.type == 'question':
					self.bt_confirmar.move(x + 100, y + 150)
					self.bt_cancelar.move(x + 300, y + 150)

	def paintEvent(self, event):

		s = self.size()
		qp = QtGui.QPainter()
		qp.begin(self)
		qp.setRenderHint(QtGui.QPainter.Antialiasing, True)
		qp.setPen(self.penColor)
		qp.setBrush(self.fillColor)
		qp.drawRect(0, 0, s.width(), s.height())

		qp.setPen(self.popup_penColor)
		qp.setBrush(self.popup_fillColor)
		
		if not self.frame:
			ow = int(s.width()/2-self.popup_width/2)
			oh = int(s.height()/2-self.popup_height/2)
			qp.drawRoundedRect(ow, oh, self.popup_width, self.popup_height, 5, 5)

		font = QtGui.QFont()
		font.setPixelSize(14)
		font.setBold(True)
		qp.setFont(font)
		qp.setPen(QtGui.QColor(70, 70, 70))

		if self.type != 'loading':
			qp.drawText(event.rect(), Qt.AlignCenter, self.text)

		qp.end()

	def quit(self):
		self._onclose()

	def _onclose(self):
		#self.SIGNALS.CLOSE.emit()
		self.close()
		return self.retorno

class Exemple(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super(Exemple, self).__init__(parent)

		self._popup = QtWidgets.QPushButton("Show de Popup!!!")
		self._popup.setFixedSize(150, 40)
		self._popup.clicked.connect(self._onpopup)

		self._other1 = QtWidgets.QPushButton("A button")
		self._other2 = QtWidgets.QPushButton("A button")
		self._other3 = QtWidgets.QPushButton("A button")
		self._other4 = QtWidgets.QPushButton("A button")

		hbox = QtWidgets.QHBoxLayout()
		hbox.addWidget(self._popup)
		hbox.addWidget(self._other1)
		hbox.addWidget(self._other2)
		hbox.addWidget(self._other3)
		hbox.addWidget(self._other4)
		self.setLayout(hbox)

		self._popframe = None
		self._popflag = False
		self.ret = None

	def resizeEvent(self, event):
		if self._popflag:
			self._popframe.move(0, 0)
			self._popframe.resize(self.width(), self.height())

	def _onpopup(self):
		self._popframe = PopUpWidget(self)
		self._popframe.move(0, 0)
		self._popframe.resize(self.width(), self.height())
		self._popframe.SIGNALS.CLOSE.connect(self._closepopup)
		self._popflag = True
		self._popframe.show()

	def _closepopup(self):
		self.ret = self._popframe.retorno
		self._popframe.close()
		self._popflag = False
		
	def retorno(self):
		print(self._popframe.retorno)


if __name__ == '__main__':
	import sys
	app = QtWidgets.QApplication(sys.argv)
	main = Exemple()
	main.resize(500, 500)
	main.show()
	sys.exit(app.exec_())