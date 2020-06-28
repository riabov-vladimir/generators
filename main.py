from application.functions import json_file_print, json_to_file, get_country_names
from application.md_5_generator import md5_from_file_genegator
from application.country_iter import CountryIterator

if __name__ == '__main__':

	"""______________________________________ЗАДАЧА №1____________________________________________"""

	reader = json_file_print()                   # десериализуем json-файл с данными о странах

	country_names = get_country_names(reader)    # достаём из него список названий всех стран

	for item in CountryIterator(country_names):  # итерируемся по списку
		json_to_file(item)                       # пишем результаты в файл

	"""______________________________________ЗАДАЧА №2______________________________________________"""

	for line in md5_from_file_genegator():
		print(line)
