import json
from pprint import pprint
import wikipediaapi

# def print_json_file(input_file='C:/Users/79055/PycharmProjects/generators/data/countries.json'):
# 	"""Функция для десериализации json файлов"""


if __name__ == '__main__':

	input_file = 'C:/Users/79055/PycharmProjects/generators/data/countries.json'
	wiki_wiki = wikipediaapi.Wikipedia('en')

	with open(input_file, encoding='utf-8') as file:

		reader = json.load(file)

		for country in reader:
			country_name = country['name']['common']
			country_name_underscored = country_name.replace(' ', '_')
			country = wiki_wiki.page(country_name_underscored)
			try:
				print(f'{country_name} -- {country.fullurl}')
			except KeyError:
				print(f'Bad request for "{country_name}" (got KeyError)')