from application.functions import json_file_print, json_to_file, get_country_names
from pprint import pprint
# from application.country_iter import country_iter
from application.country_iter import CountryIterator

if __name__ == '__main__':
	reader = json_file_print()                   # десериализуем json-файл с данными о странах

	country_names = get_country_names(reader)    # достаём из него список названий всех стран

	for item in CountryIterator(country_names):  # итерируемся по списку
		json_to_file(item)                       # пишем результаты в файл
