import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QMainWindow

from src.controller.lib.ssqt import SSQt
from src.controller.widgets.popup import PopUpWidget

SSQt.load_uifile(True, 'src/view/singleview/ui/singleviewapp.ui')
from src.view.singleview.ui.singleviewapp import Ui_SingleViewApp

class SingleViewAppView(QMainWindow, Ui_SingleViewApp, SSQt):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		# Atributos para o Dialog
		self.popUpDialog = PopUpWidget(self)
		self.popUpDialogFlag = False
		
		#Atributos para o Finder
		#self.popUpFrame = PopUpWidget(self)
		self.popUpFrameFlag = False

	def resizeEvent(self, event):
		if self.popUpDialogFlag:
			self.popUpDialog.move(0, 0)
			self.popUpDialog.resize(self.width(), self.height())
			
		if self.popUpFrameFlag:
			self.popUpFrame.move(0, 0)
			self.popUpFrame.resize(self.width(), self.height())

	def onPopupDialog(self, text='', type=None):
		self.popUpDialog.inicialize(text=text, type=type, frame=None, data=None)
		self.popUpDialog.move(0, 0)
		self.popUpDialog.resize(self.width(), self.height())
		self.popUpDialogFlag = True
		self.popUpDialog.show()

	'''
	def onpopUpFrame(self, frame=None):
		self.popUpFrame.inicialize(frame=frame)
		self.popUpFrame.move(0, 0)
		self.popUpFrame.resize(self.width(), self.height())
		self.popUpFrameFlag = True
		self.popUpFrame.show()
	'''

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = SingleViewAppView()
	w.show()
	sys.exit(app.exec_())
