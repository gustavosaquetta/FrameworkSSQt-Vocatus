'''
Created on 12 de out de 2017

@author: gustavosaquetta
'''
import sys, os
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QTextEdit
from PyQt5.Qt import QPrintPreviewDialog, Qt, QApplication
class DataToPreview(object):

	def __init__(self):
		'''
		Constructor
		'''
		self.text_editor = QTextEdit()

	def onPrintPreview(self):
		"""
		Exibe o preview com o relatório de acordo com layout
		"""
		txt = '-'*100000
		self.text_editor.setText(txt)
		dialog = QPrintPreviewDialog()
		dialog.setWindowState(Qt.WindowMaximized)
		dialog.paintRequested.connect(self.text_editor.print_)
		dialog.setWindowFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint | Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint | Qt.WindowContextHelpButtonHint)
		dialog.exec()

if __name__ == "__main__":
	app = QApplication(sys.argv)
	myWindow = DataToPreview()
	myWindow.onPrintPreview()
	app.exec_()