strings = ["Animals", "Badger", "Hony Bee", "Honey Badger"]
for i in strings:
    print(i.upper())
    print(i.lower())


string1 = "  Filet Mignon"
string2 = "Brisket  "
string3 = "  Chesseburger  "

print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "  bEautiful"

string1 = string1.lower()
print(string1.startswith("be"))
