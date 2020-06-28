import wikipediaapi


class CountryIterator:
	def __init__(self, country_list, start=0, end=240):
		self.wiki = wikipediaapi.Wikipedia('en')
		self.country_list = country_list
		self.start = start
		self.current = -1
		self.end = end

	def get_url(self, name):
		country = self.wiki.page(name)
		full_url = country.fullurl
		return full_url

	def __iter__(self):
		return self

	def __next__(self):
		self.current += 1
		if self.current > self.end:
			raise StopIteration
		self.result = f'{self.country_list[self.current]} -- {self.get_url(self.country_list[self.current])}'
		print(self.result)
		return self.result
