import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import * 
from PyQt5 import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *
import time
#from src.controller.widgets.spinner import WaitingSpinner

import threading
import time

if __name__ == "__main__":
	import sys, time
	
	#Define estilo padrão
	app = QApplication(sys.argv)
	app.setStyle(QStyleFactory.create('Fusion'))
	
	# Define variaveis de ambiente
	if '--compile' in sys.argv:
		os.environ.update({'compileUi':'1'})
		os.environ.update({'compileDb':'1'})

	if '--compileui' in sys.argv:
		os.environ.update({'compileUi':'1'})

	if '--compiledb' in sys.argv:
		os.environ.update({'compileDb':'1'})
	
	
	# Create and display the splash screen
	splash_pix = QPixmap('assets/images/splash.jpg')
	splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
	splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
	splash.setEnabled(False)
	splash = QSplashScreen(splash_pix)
	# adding progress bar
	progressBar = QProgressBar(splash)
	progressBar.setMaximum(100)
	progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)
	progressBar.setValue(0)
	splash.setMask(splash_pix.mask())

	'''	
	spinner = WaitingSpinner(
								splash,
								roundness=19.0, 
								opacity=15.0,
								fade=70.0, 
								radius=8.0, 
								lines=8,
								line_length=30.0, 
								line_width=8.0,
								speed=1.0, 
								color=(0, 170, 255)
							)'''
	
	splash.show()
	'''
	def show():
		#spinner.start()
		pass

	import threading
	t = threading.Thread(target=show)
	t.start()
	#import pdb;pdb.set_trace()'''
	
	splash.showMessage("<font color='blue'>Bem vindo ao Vocatus</font>", Qt.AlignCenter | Qt.AlignCenter, Qt.black)
		
	for i in range(1, 101):
		progressBar.setValue(i)
		t = time.time()

		if i == 25:
			from src.view.widgets import __init__
			splash.showMessage("<font color='blue'>Carregando configurações de usuário...</font>", Qt.AlignBottom | Qt.AlignCenter, Qt.black)

		if i == 50:
			splash.showMessage("<font color='blue'>Carregando estrutura de dados...</font>", Qt.AlignBottom | Qt.AlignCenter, Qt.black)
			from src.controller.main import MainController

		if i == 75:
			splash.showMessage("<font color='blue'>Carregando interface de usuário...</font>", Qt.AlignBottom | Qt.AlignCenter, Qt.black)

		while time.time() < t + 0.005:
		   app.processEvents()

	# Simulate something that takes time
	time.sleep(0.5)
	#splash.close()
	
	w = MainController().show()
	splash.close()
	sys.exit(app.exec_())