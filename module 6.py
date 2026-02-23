#1
import random
def roll_dice():
    return random.randint(1, 6)

result = 0
while result != 6:
    result = roll_dice()
    print(result)
#2
import random

def roll_dice(sides):
    return random.randint(1, sides)

sides = int(input("Enter number of sides on the dice: "))

result = 0
while result != sides:
    result = roll_dice(sides)
    print(result)
#3
def gallons_to_liters(gallons):
    return gallons * 3.785


while True:
    gallons = float(input("Enter gallons (negative number to stop): "))

    if gallons < 0:
        break

    liters = gallons_to_liters(gallons)
    print("Liters:", liters)
#4
def sum_list(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
result = sum_list(numbers)
print("Sum:", result)
#5
def remove_odd(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

new_numbers = remove_odd(numbers)

print("Original list:", numbers)
print("Even numbers only:", new_numbers)

#6
import math

def unit_price(diameter_cm, price):
    radius_m = (diameter_cm / 100) / 2
    area = math.pi * radius_m * radius_m
    return price / area

# Pizza 1
d1 = float(input("Enter diameter of pizza 1 (cm): "))
p1 = float(input("Enter price of pizza 1 (€): "))

# Pizza 2
d2 = float(input("Enter diameter of pizza 2 (cm): "))
p2 = float(input("Enter price of pizza 2 (€): "))

u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)

print("Pizza 1 unit price:", u1)
print("Pizza 2 unit price:", u2)

if u1 < u2:
    print("Pizza 1 gives better value.")
else:
    print("Pizza 2 gives better value.")