import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QWidget

from src.controller.lib.ssqt import SSQt

SSQt.load_uifile(True, 'src/view/cadastro/ui/empresa.ui')
from src.view.cadastro.ui.empresa import Ui_Empresa

class EmpresaView(QWidget, Ui_Empresa, SSQt):
	def __init__(self):
		super(EmpresaView, self).__init__()
		self.setupUi(self)
		self.ui()
		self.nome.textChanged.connect(self.validate_obrigatory_field)
		self.nome.textChanged.emit(self.nome.text())

		self.codigo.valueChanged.connect(self.validate_obrigatory_field)
		self.codigo.valueChanged.emit(self.codigo.value())

		self.cpf.textChanged.connect(self.validate_obrigatory_field)
		self.cpf.textChanged.emit(self.cpf.text())

if __name__ == "__main__":
	app = QApplication(sys.argv)
	w = EmpresaView()
	w.show()
	sys.exit(app.exec_())
