def main():
	famous_person = "                  Confucious                       "
	print(f"{famous_person} say: A man wrong on elevator wrong on many level")
	print(f"{famous_person.rstrip()} say: A man wrong on elevator wrong on many level")
	print(f"{famous_person.lstrip()} say: A man wrong on elevator wrong on many level")
	print(f"{famous_person.strip()} say: A man wrong on elevator, wrong on many level")

if __name__ == "__main__":
	main()
