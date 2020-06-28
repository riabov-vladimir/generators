import json


def json_to_file(script_result, input_file='C:/Users/79055/PycharmProjects/generators/data/country_links.txt'):
	"""Функция для сериализации json-данных в файл 'country_links.json' """
	with open(input_file, 'a', encoding='utf-8') as output_file:
		output_file.write(script_result)
		output_file.write('\n')


def json_file_print(input_file = 'C:/Users/79055/PycharmProjects/generators/data/countries.json'):
	"""Функция для десериализации json файлов"""
	with open(input_file, encoding='utf-8') as file:
		reader = json.load(file)
	return reader


def get_country_names(reader):
	"""Фильтуем json-данные стран, получаем список названий стран"""

	country_names = []

	for country in reader:
		country_name = country['name']['common']
		country_name_underscored = country_name.replace(' ', '_')
		country_names.append(country_name_underscored)
	return country_names
