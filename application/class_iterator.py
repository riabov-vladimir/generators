import json
from pprint import pprint
import wikipediaapi

# def print_json_file(input_file='C:/Users/79055/PycharmProjects/generators/data/countries.json'):
# 	"""Функция для десериализации json файлов"""

def json_to_file(script_result):
	"""Функция для сериализации json-данных в файл 'groups.json' """
	with open('C:/Users/79055/PycharmProjects/generators/data/country_links.json', 'w', encoding='utf-8') as \
			output_file:
		json.dump(script_result, output_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':

	input_file = 'C:/Users/79055/PycharmProjects/generators/data/countries.json'
	wiki_wiki = wikipediaapi.Wikipedia('en')
	temp_dict_list = []
	with open(input_file, encoding='utf-8') as file:

		reader = json.load(file)

		for country in reader:
			country_dict = {}
			country_name = country['name']['common']
			country_name_underscored = country_name.replace(' ', '_')
			country = wiki_wiki.page(country_name_underscored)

			try:
				full_url = country.fullurl
			except KeyError:
				print(f'Bad request for "{country_name}" (got KeyError)')
			else:
				print(f'{country_name} -- {full_url}')
				country_dict[country_name_underscored] = full_url
				temp_dict_list.append(country_dict)

	json_to_file(temp_dict_list)
