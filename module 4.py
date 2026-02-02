# 1 a program thats prints out numbers divible by 3 from 1-1000
from ctypes import pythonapi

num = 1
while num <=1000:
    if num % 3 ==0:
        print(num)
    num += 1

# 2 a program that converts inches to centimeters untill user enters a negative number

while True:
    inche = float(input("enter your inche: "))
    if inche < 0:
        break
    cm = inche * 2.54
    print(cm)

# 3 a program that ask for numbers untill empty input then prints largest and smallest

numbers = []
while True:
    value = int(input("enter your value (nothing to stop): "))
    if value =="":
        break
    numbers.append(float(value))
print("smallest" , min(numbers))
print("largest", max(numbers))

# 4 guessing game numbers

import random
numbers = random.randint(1, 10)
while True:
    guess = int(input("enter your guess: "))
    if guess > numbers:
        print("too high")
    elif guess < numbers:
        print("too low")
    else:
        print("you guessed right")
        break

# 5 a program for username and password max 5 attempt.

username = python
password = rules
attempts = 0

while attempts > 5:
     username = input("enter your username: ")
     password = input("enter your password: ")
     if username == "python" and password == "rules":
         print("welcome " + username)
         break
     else:
         print("wrong username or password")
         attempts += 1
     if attempts == 5:
         print("you are blocked")

# 6 a program to approximate pi using random points

import random
inside = 0
total = 10000
count = 0
while count < total:
    h
