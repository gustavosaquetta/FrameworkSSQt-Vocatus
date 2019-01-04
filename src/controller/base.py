from PyQt5.QtCore import QCoreApplication
from collections import namedtuple
from src.controller.lib.ssqt import SSQt

class Base:
	#def __ini__(self):
	#	Super().__init__()

	def wait_return(self, obj):
		if hasattr(obj, 'view') and hasattr(obj.view, 'centralwidget'):
			obj.view.centralwidget.setEnabled(False)

		i = 0
		while ( obj.retorno_frame == -1 ):
			# not doing anything                                                                                                                                                                                                   
			if ( i % 100000 == 0 ):
				print("Aguardando retorno: ", obj.retorno_frame)
			QCoreApplication.processEvents()
			i += 1;
		print("Retorno recebido: ", obj.retorno_frame)
		ret = obj.retorno_frame
		obj.retorno_frame = -1
		
		if hasattr(obj, 'view') and hasattr(obj.view, 'centralwidget'):
			obj.view.centralwidget.setEnabled(True)
		return ret
		
	def dictToClass(self, d, name):
		return namedtuple(name, d.keys())(*d.values())
	