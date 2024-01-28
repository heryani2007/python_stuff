def main():
	countries = []
	country_counter = {}
	while True:
		country = input("If you could visit: ")
		countries.append(country)
		if country in countries:
			country_counter[country] = countries.count(country)
#				print (f"{country} {country_counter}")
#				print(countries)
			print (country_counter)

if __name__ == "__main__":
	main()
