import sys
email = sys.argv[1].strip()

if "@" in email:
    print("Valid")
else:
    print("Invalid")

