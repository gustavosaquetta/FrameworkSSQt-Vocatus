
'''
Created on 12 de out de 2017

@author: gustavosaquetta
'''
import sys, os, tempfile, subprocess
sys.path.append(os.getcwd())
from operator import itemgetter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

class DataToPdf():
	"""
	Exporta um modelo de dados para PDF.
	"""
	
	def __init__(self, fields=None, data=None, title=None, filters=None, results=None, sort_by=None):
		"""
		Arguments:
			fields  - tupla com os ((nome_campo/key, nome da coluna 'tela')) 
			data    - Lista de dicionários.
			title   - Titulo do relatório.
			filters - Nome dos filtro utilizados em tela.
			results - Dicionario com os resultados.
			sort_by - Tupla com (sort_key, sort_order).
		"""
		if not data or not fields:
			print('Campos obrigatórios não informados!')
			return

		self.fields = fields
		self.data = data
		self.title = title
		self.filters = filters
		self.results = results
		self.sort_by = sort_by
		
	def export(self, filename=None, data_align='LEFT', table_halign='LEFT'):
		"""
		Exporta os dados para o PDF.
		
		parametros:
			filename - Nome do arquivo.
			data_align - tipos de alinhamento (ex. 'LEFT', 'CENTER', 'RIGHT')
			table_halign - alinhamento da tabela (ex. 'LEFT', 'CENTER', 'RIGHT')
		"""
		if not filename:
			dir ='/tmp'
			if os.name == 'nt':
				dir ='c:\\temp'

			filename = tempfile.NamedTemporaryFile(prefix='_report', suffix='.pdf', dir=dir, delete=False)

		doc = SimpleDocTemplate(filename.name, pagesize=A4, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)

		styles = getSampleStyleSheet()
		styleH = styles['Heading1']
		normal = styles["Normal"]
		styles.wordWrap = 'CJk'

		story = []

		if self.title:
			story.append(Paragraph(self.title, styleH))
			story.append(Spacer(1, 0.10 * inch))

		if self.filters:
			for filter in self.dict_to_string(self.filters):
				story.append(Paragraph(filter, normal))
				story.append(Spacer(1, 0.1 * inch))
			
		if self.sort_by:
			reverse_order = False
			if (str(self.sort_by[1]).upper() == 'DESC'):
				reverse_order = True

			self.data = sorted(self.data,
							   key=itemgetter(self.sort_by[0]),
							   reverse=reverse_order)

		converted_data = self.__convert_data()

		#TODO aqui deve vir na tupla o tamanho de cada carinha

		col_list = [x[1] for x in self.fields]
		table = Table(converted_data, hAlign=table_halign, colWidths=col_list)
		
		table.setStyle(TableStyle([
			('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
			('ALIGN', (0, 0), (-1, 0), 'CENTER'),
			('ALIGN',(0, 0),(0,-1), data_align),
			('INNERGRID', (0, 0), (-1, -1), 0.50, colors.black),
			('BOX', (0,0), (-1,-1), 0.25, colors.black),
		]))
		
		story.append(table)
		
		if self.results:
			for result in self.dict_to_string(self.results):
				story.append(Paragraph(result, normal))
				story.append(Spacer(1, 0.1 * inch))
		
		doc.build(story)
		
		if os.name == 'nt':
			os.startfile(filename.name)
			#subprocess.Popen([filename.name],shell=True)
		else:
			os.system('open %s' % filename.name)

	def __convert_data(self):
		"""
		Converte o dicionário em listas e as listas geram a tabela do PDF.
		"""

		keys, names = zip(*[[k[0], k[1]] for k, n in self.fields])
		new_data = [names]
		
		for d in self.data:
			new_data.append([d[k] for k in keys])
			
		return new_data

	def dict_to_string(self, dict, concatenate=':'):
		items = dict.items()
		list = []
		for item in items:
			msg = '%s%s %s' % (item[0].upper(), concatenate, item[1])
			list.append(msg)
		return list

if __name__ == "__main__":
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
	
	DTP = DataToPdf(fields, data, sort_by=('size', 'DESC'), title=title, filters=filters, results=results)
	DTP.export()