def main(name="Default Value"):
	print(name)

_ = input("Name: ")
if len(_) > 0:
	main(_)
else:
	main()
