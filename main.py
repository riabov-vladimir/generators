from application.functions import json_file_print, json_to_file, get_country_names
from pprint import pprint
# from application.country_iter import country_iter
from application.iterator_draft import CountryIterator

if __name__ == '__main__':
	reader = json_file_print()

	country_names = get_country_names(reader)

	for item in CountryIterator(country_names):
		json_to_file(item)
