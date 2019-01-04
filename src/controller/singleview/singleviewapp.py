import os, sys
sys.path.append(os.getcwd())

from PyQt5.QtWidgets import QApplication, QStyleFactory

from src.view.singleview.singleviewapp import SingleViewAppView

from src.controller.cadastro.empresa import EmpresaController
from src.controller.singleview.login import LoginController
from src.controller.configuracoes.database import DatabaseController
from src.controller.configuracoes.look_and_feel import LookController
from src.controller.base import Base

from src.controller.widgets.popup import PopUpWidget

class SingleViewAppController(Base):
	def __init__(self, env, force_show=None):
		super(Base, self).__init__()
		self.env = env
		self.view = SingleViewAppView()
		
		self.classe = None
		self.isExpance = True
		self.retorno_frame = -1
		self.current_frame = None
		
		#chama o login a primeira tela do sistema :)
		self.ctrlLogin = LoginController()
		self.executeLogin()
		self.ctrlLogin.view.bt_login.clicked.connect(self.loginListner)
		self.view.bt_expance_layout.clicked.connect(self.expanceLayout)

		# Conecta os botões dos dialogs com a tela principal
		self.view.popUpDialog.bt_confirmar.clicked.connect(self.on_bt_pop_ret)
		self.view.popUpDialog.bt_cancelar.clicked.connect(self.on_bt_pop_ret)
		self.view.popUpDialog.bt_close.clicked.connect(self.on_bt_pop_ret)

		#self.view.popUpFrame.bt_confirmar.clicked.connect(self.on_bt_pop_finder_ret)
		#self.view.popUpFrame.bt_cancelar.clicked.connect(self.on_bt_pop_finder_ret)
		
		# Força a saida da tela pré instanciada
		self.view.popUpDialog.on_bt_sair()
		#self.view.popUpFrame.on_bt_sair()
		
		
		# se pro sivio, sempre e sempre passar o parrent pode ser muito util porra!
		# perdi mais de 20horas no total me matando com as porras das telas filhas aff :/ já fui bem melhorzinho
		self.menu_dict = {
					'bt_database':('DatabaseController(self, self.env)', 'ctrlDatabase'),
					'bt_empresa': ('EmpresaController(self, self.env)','ctrlEmpresa'),
					'bt_look': ('LookController(self, self.env)','ctrlLook'),
					}

		for menu in self.menu_dict.items():
			#C = eval(menu[1][0])
			#getattr(self, menu[1][1]) = C
			getattr(self.view, menu[0]).clicked.connect(self.menu_option)
			
			# se ficar muito pesado pode remover esta linha, cria uma atributo para cada tela
			setattr(self, menu[1][1], eval(menu[1][0]))

		#self.ctrlLook.ctrlButtonsCC.view.bt_confirmar.clicked.connect(self.load_look)

		# Connects feitos na mão para testes
		self.view.bt_home.clicked.connect(lambda: self.onPopupDialog(text='Nani?!', type='info'))
		self.view.bt_preview.clicked.connect(self.onPreview)
		self.view.bt_pdf.clicked.connect(self.onPdf)

		# Definine o estilo visual do sistema
		self.load_look()

		if force_show:
			self.view.show()

	def show(self):
		return self.view
		
	def menu_option(self):
		sender = self.view.sender().objectName()
		# me custou 7 horas para aprender isso!!!
		# toda classe que irá compor a tela deve ser declarada
		# dentro de um objeto dentro do self. é um bug de versão!
		# exemplo abaixo
		self.classe = eval(self.menu_dict[sender][0])
		#self.updaterFrame(self.classe.show())

		setattr(self, self.menu_dict[sender][1], self.classe)

		#talvez precise ser um self... para nao dar erro!
		child = getattr(self, self.menu_dict[sender][1])
		#TODO fazer algo para nao instanciar a mesma classe mais de uma vez!
		#self.view.pdb()
		#if self.current_frame and (self.current_frame.__class__ == child.view.__class__ or self.current_frame.__class__ == child.__class__):
		#	return

		self.updaterFrame(child.show())


	def resizeEvent(self, event):
		if self.popUpDialogFlag:
			self.popUpDialog.move(0, 0)
			self.popUpDialog.resize(self.view.width(), self.view.height())

	def updaterFrame(self, new_frame):
		self.current_frame = new_frame
		self.view.main_label.setText(self.current_frame.windowTitle())
		
		self.clearLayout(self.view.horizontalLayout)
		self.view.horizontalLayout.addWidget(self.current_frame)

	def clearLayout(self,layout=None):
		if not layout:
			layout = self.view.horizontalLayout
		while layout.count():
			child = layout.takeAt(0)
			if child.widget():
				child.widget().deleteLater()

	def executeLogin(self):
		self.view.line.hide()
		self.view.bt_home.hide()
		self.view.status_frame.hide()
		self.view.scrollArea.hide()
		#talvez remover
		self.updaterFrame(self.ctrlLogin.show())

	def onLogin(self):
		self.view.line.show()
		self.view.bt_home.show()
		self.view.status_frame.show()
		self.view.scrollArea.show()
		del(self.ctrlLogin)
		
	def loginListner(self):
		print('Login SingleView')
		if self.ctrlLogin.auth:
			self.onLogin()
			self.clearLayout()

	def expanceLayout(self):
		if self.isExpance and self.current_frame:
			self.view.bt_home.hide()
			self.view.bt_expance_layout.setText('>>')
			self.view.scrollArea.hide()
			self.view.line.hide()
			self.isExpance = False
		else:
			self.view.bt_home.show()
			self.view.bt_expance_layout.setText('<<')
			self.view.scrollArea.show()
			self.view.line.show()
			self.isExpance = True

	def load_look(self):
		CL = LookController()
		if CL.set_look():
			style, look = CL.set_look()
			QApplication.setStyle(QStyleFactory.create(look))
			self.view.setStyleSheet(look)
	
	def onPopupDialog(self, text='', type=None):
		self.view.onPopupDialog(text=text, type=type)

	def on_bt_pop_ret(self):
		print('Dialog ', self.view.popUpDialog.retorno)
		return self.view.popUpDialog.retorno
		
	def onpopUpFrame(self, frame=None, data=None):
		self.view.popUpFrame = PopUpWidget(self.view)
		self.view.popUpFrame.inicialize(frame=frame, data=data)

		self.view.popUpFrame.bt_confirmar.clicked.connect(self.on_bt_pop_finder_ret)
		self.view.popUpFrame.bt_cancelar.clicked.connect(self.on_bt_pop_finder_ret)

		self.view.popUpFrame.move(0, 0)
		self.view.popUpFrame.resize(self.view.width(), self.view.height())
		self.view.popUpFrameFlag = True
		self.view.popUpFrame.show()

	def on_bt_pop_finder_ret(self):
		#print('Finder ', self.view.popUpDialog.retorno)
		#return self.view.popUpDialog.retorno
		print('Finder############# ', self.view.popUpFrame.retorno)
		self.retorno_frame = self.view.popUpFrame.retorno
		return self.view.popUpFrame.retorno

	def onPreview(self):
		from src.controller.reports.simple_preview import DataToPreview
		DTP = DataToPreview()
		DTP.onPrintPreview()

	def onPdf(self):
		from src.controller.reports.simple_pdf import DataToPdf
		
		title='Alpha vaca'
		data = []
		for x in range(0,10):
				data.append({'filename': 'nome',
				 'filepath': 'tamanho00000000000000000000000',
				 'size': 'tamanhus',
				 'mtime': 'horario'})
		
		fields = (
			(('filename', 'Filename'), 100),
			(('filepath', 'Filepath'), 200),
			(('size', 'Size (KB)'), 100),
			(('mtime', 'Modified'), 100),
		)
		
		filters = {	
					'Empresa': 'Minha',
					'Periodo': 'xx/xx/xxx e yy/yy/yyyy',
					'Pessoa':  'gustavo',
					'Produto': 'camiseta polo tommy',
				}
		
		results = {	
					'Total de prodtutos': '1000', 
					'Total liquido': '900', 
					'Total bruto':  '1200', 
					'Total de serviços': 100, 
				}
		
		DTP = DataToPdf(fields, data, title=title, filters=filters, results=results)
		DTP.export()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	w = SingleViewAppController(force_show=True)
	sys.exit(app.exec_())