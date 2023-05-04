import csv
"""while True:
    name = input("What's your name? ")
    file = open("name.txt", 'a')
    file.write(f"{name}\n")"""

"""while True:
    try:
        name = input("what's your name? ")
        with open("names.txt", 'a') as file:
            file.write(f"{name}\n")
    except KeyboardInterrupt:
        pass"""
"""names = []
with open("names.txt", 'r') as files:
    for line in files:
        names.append(line)
        
for i in sorted(names):
    print(f"Hello ", i.rstrip())"""

"""files = open("names.txt")
for lines in sorted(files):
    print("Hello ", lines, end='')"""
"""try:
    while True:
        s = input("What's your name, class? ")
        with open("students.csv", 'a') as students:
            students.write(f"{s}\n")
except KeyboardInterrupt:
    pass"""

"""with open("students.csv", 'r') as file:
    for i in sorted(file):
        name, sch = i.rstrip().split(',')
        print(f"{name} is in {sch}")"""
"""students = []
with open("students.csv") as file:
    # for line in sorted(file):
    #     name, house = line.rstrip().split(',', maxsplit=2)
    # readers = csv.reader(file)
    # for name, house in readers:
    #     student = {'name': name, 'house': house}
        # students.append({'name': name, 'house': house})
    readers = csv.DictReader(file)
    for row in readers:
        students.append({"name": row["name"], "house":row["house"]})

for i in sorted(students, key=lambda i: i['house']):
    print(f"{i['name']} is in {i['house']}")"""

"""name = input("What's your name? ")
home = input("Where's your house? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'home'])
    writer.writerow({'name': name, 'home': home})"""



