import os, sys
sys.path.append(os.getcwd())

from src.controller.environment import Environment
DB = Environment().db
database = DB.connect(autocommit=True)

sequence_list = [
					'general_id_seq',
				]

for sequence in sequence_list:
	if database and not database.sequence_exists(sequence):
		database.create_sequence(sequence)