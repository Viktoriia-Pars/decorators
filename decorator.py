import hashlib
import datetime
import json
from pprint import pprint


def decor(foo):
	def new_foo(*args, **kwars):
		result = foo(*args, **kwars)
		with open('logs.json', 'w') as logs_file:
			d = datetime.datetime.today().replace(microsecond=0)
			log = {"дата": f'{d}', "имя функции": f'{foo.__name__}', "аргументы": f'{args, kwars}', "результат": f'{result}'}
			json.dump(log, logs_file, ensure_ascii=False)
		print(logs_file)

		with open('logs.json', 'r') as f:
			json_data = json.load(f)
			pprint(json_data)

		return result

	return new_foo

# @decor
# def get_hash(path: str):
# 	with open(path, 'rb') as file:
# 		for line in file:
# 			yield hashlib.md5(line).hexdigest()


def parametrized_decor(path_logs):
	path_logs  = input('введите путь до папки ')
	def decor(foo):
		def new_foo(*args, **kwars):
			nonlocal path_logs
			result = foo(*args, **kwars)
			with open(path_logs +'\logs.json', 'w') as logs_file:
				d = datetime.datetime.today().replace(microsecond=0)
				log = {"дата": f'{d}', "имя функции": f'{foo.__name__}', "аргументы": f'{args, kwars}',
					   "результат": f'{result}'}
				json.dump(log, logs_file, ensure_ascii=False)

			return result

		return new_foo
	return decor


@parametrized_decor(path_logs=None)
def get_hash(path: str):
	with open(path, 'rb') as file:
		for line in file:
			yield hashlib.md5(line).hexdigest()
	pass

for hash_string in get_hash('text.txt'):
		print(hash_string)
