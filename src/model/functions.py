import os, sys
sys.path.append(os.getcwd())

from src.controller.environment import Environment
DB = Environment().db
database = DB.connect()

general_id = 'CREATE OR REPLACE FUNCTION public.general_id( '\
				'integer, '\
				'integer) '\
				'RETURNS bigint AS '\
				'$BODY$ '\
				'select int8(int8($1) * 4294967296::int8) + int8($2) '\
				'$BODY$ '\
				'LANGUAGE sql VOLATILE '\
				'COST 100; '\
				'ALTER FUNCTION public.general_id(integer, integer) '\
				'OWNER TO postgres;'

try:
	database.execute_sql(general_id).execute()
except:
	pass