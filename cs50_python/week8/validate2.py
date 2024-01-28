email = input("Email: ").strip()

username, domain = email.split("@")
if (len(username) + len < 2):

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
