 # question 1 ask for a name and great the user.
"""
letters = input("enter your letters: ")
if letters in ("a","e","i","o","u"):
 print("this is a vowel")
elif letters ==('y'):
 print("this could be a vowel or consonant")
else:
 print("this is a consonant")


name = input("enter your name: ")
print(f"hello, {name}!")

# question 2 a program to print out area of a circle after taking radius.

import math as m
radius = float(input("enter your radius: "))
area = m.pi * radius ** 2
print(f"the area is: {area}")

# question 3 a program that uses the length and wide of a triangle to print out the perimeter and area.

length = float(input("enter your length: "))
width = float(input("enter your width: "))
perimeter = 2 * (length + width)
area = length * width
print(f"the perimeter is: {perimeter}")
print(f"the area is: {area}")

# question 4 a program that asks for 3 integer, and produces the sum product and average

a = int(input("enter number 1: "))
b = int(input("enter number 2: "))
c = int(input("enter number 3: "))
sum_numbers = a + b + c
prod = a * b * c
average = sum_numbers / 3
print(f"the sum is: {sum_numbers}")
print(f"the prod is: {prod}")
print(f"the average is: {average}")

# question 5 a program that takes mass in medieval unit and converts to kilogram and grams for the user.

talent = int(input("enter your talent: "))
pounds = int(input("enter your pounds: "))
lots = int(input("enter your lots: "))



# question 6 a program that draws two random combinations of numbers for a combination lock



letters = input("enter your letters: ")
if letters == ("a","e","i","o","u"):
 print("this is a vowel")
elif letters ==('y'):
 print("this could be a vowel or consonant")
else:
 print("this is not a vowel or consonant")

"""

import random
number = random.randint(1,100)
guess = 0
while guess != number:
    guess = int(input("enter your guess: "))
    if guess > number:
        print("your guess is too high")
    elif guess < number:
        print("your guess is too low")
    else:
        print("your guess is correct")




