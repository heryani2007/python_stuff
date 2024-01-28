def main():
    i = int(input("num: "))
    yield "🐑" * i

# To use the generator, you need to iterate over it
for sheep_string in main():
    print(sheep_string)
