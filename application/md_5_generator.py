from hashlib import md5


def md5_from_file_genegator(input_file='C:/Users/79055/PycharmProjects/generators/data/country_links.txt'):
	with open(input_file, 'r', encoding='utf-8') as input_file:
		for line in input_file:
			yield md5(line.encode()).hexdigest()

