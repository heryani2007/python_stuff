def main():
	countries = []
	countries_counter = {}
	while True:
		country = input("Dream Vecation: ")
		countries.append(country)
		for country in countries:
			countries_counter[country] = countries.count(country)
		print(f"{countries_counter}")
if __name__ == "__main__":
	main()
