#1 a program that requires the fish caught to be 42 centimeters or longer to meet requirements

fishlenght = int(input("enter fish length (cm): "))
if fishlenght < 42:
    print("release this fish.")
    print("this is", 42 - fishlenght, "cm below size.")
else:
     print("this is perfect")

#2 a program that ask the user to enter the cabin class and prints out location on deck

cabinclass = input("enter cabin class: ").lower().upper()
if cabinclass =="LUX":
    print("upper-deck cabin with a balcony")
elif cabinclass == "A":
    print("above the car deck, equiped with a window.")
elif cabinclass == "B":
    print("windowless cabin above the car deck.")
elif cabinclass == "C":
    print("windowless cabin below the car deck.")
else:
    print("cabin class not recognized.")


#3 programs that asks for gender and hemoglobin value and returns if value ids too high or low and range for male and female

gender = input("enter gender (male/female): ")
hb = float(input("enter hemoglobin level : "))

if gender == "male":
    if hb < 134:
        print("hemoglobin level is too low.")
    elif hb > 167:
        print("hemoglobin level is too high.")
    else:
        print("hemoglobin level is normal.")
elif gender == "female":
    if hb < 117:
        print("hemoglobin level is too low.")
    elif hb > 156:
        print("hemoglobin level is too high.")
    else:
        print("hemoglobin level is normal.")


#4 a program to determine the leap year after asking the year from the user

year = int(input("enter year: "))
if year % 400 == 0:
    print("leap year.")
elif year % 100 == 0:
    print("not leap year.")
elif year % 4 == 0:
    print("leap year.")
else:
    print("not leap year.")




