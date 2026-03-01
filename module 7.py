# question 1
seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month number (1-12): "))

if month in (12, 1, 2):
    print(seasons[0])
elif month in (3, 4, 5):
    print(seasons[1])
elif month in (6, 7, 8):
    print(seasons[2])
elif month in (9, 10, 11):
    print(seasons[3])
else:
    print("Invalid month")

# question 2
names = set()

while True:
    name = input("Enter name (empty to stop): ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nNames entered:")
for n in names:
    print(n)

# question 3
airports = {}

while True:
    print("\n1 = Add airport")
    print("2 = Get airport name")
    print("3 = Quit")

    choice = input("Choose option: ")

    if choice == "1":
        icao = input("Enter ICAO code: ")
        name = input("Enter airport name: ")
        airports[icao] = name

    elif choice == "2":
        icao = input("Enter ICAO code: ")
        if icao in airports:
            print("Airport name:", airports[icao])
        else:
            print("Airport not found.")

    elif choice == "3":
        break

    else:
        print("Invalid option")
