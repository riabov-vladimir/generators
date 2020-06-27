import json
from pprint import pprint


# def print_json_file(input_file='C:/Users/79055/PycharmProjects/generators/data/countries.json'):
# 	"""Функция для десериализации json файлов"""


if __name__ == '__main__':

	input_file = 'C:/Users/79055/PycharmProjects/generators/data/countries.json'

	with open(input_file, encoding='utf-8') as file:

		reader = json.load(file)

		for country in reader:
			print(country['name']['official'])

	# pprint(reader)

