import re

def main():
    url = input("URL: ").strip()#.lower()
    username = re.sub(r"^(http(s)?://)?(www\.)?twitter\.com/", "", url)
    if "twitter" in url:
        print(f"{username}")
    else:
        print("Invalid URL")

if __name__ == "__main__":
    main()
