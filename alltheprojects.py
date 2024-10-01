from time import sleep
from random import randint
import sys
import winsound
from winsound import PlaySound
import random
letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ';', ':', '/', '?', '.', '>']
num = 0
answer = "None"
result = 0
def calc():
 print("CALCULATOR")
 a = int(input("First num: "))
 b = int(input("Second num: "))
 c = input("Select action: ")
 if(c == "+"):
    print("The result is...")
    sleep(2)
    print(a + b)
 if(c == "-"):
    print("The result is...")
    sleep(2)
    print(a - b)

 if(c == "*"):
    print("The result is...")
    sleep(2)
    print(a * b)
 if(c == "/"):
    print("The result is...")
    sleep(2)
    print(a / b)
def alert():
    print("ALERT")
    duration = int(input("Enter time (In seconds): "))
    print(f"Arert set up for {duration} seconds!")
    sleep(duration)
    print("ALERT!!!")
    PlaySound('SystemAsterisk', winsound.MB_OK)
def passgen():
    print("PASSWORD GENERATOR")
    print(f"I generated a reliable password for you: {random.choice(letters)}{random.choice(letters)}{random.choice(num1)}{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}{random.choice(symbols)}{random.choice(num1)}{random.choice(num1)}{random.choice(symbols)}")
def miles_to_km():
 print("MILES TO KILOMETERS CONVERTER") 
 amount = int(input("Please enter the amount of miles... "))
 result = amount * 1.609344
 print(f"The result is {result}")
def km_to_miles():
 print("KILOMETERS TO MILES CONVERTER")
 amount = int(input("Please, enter the amount of kilometers... "))
 result = amount * 0.621371192
 print(f"The result is {result}")
def converter():
   print("CONVERTER")
   answer = input("""
   PLEASE, SELECT THE CONVERTION
   - Miles to km
   - km to miles
   """)
   if answer == "miles to km":
    miles_to_km()
   if answer == "km to miles":
    km_to_miles()

print("PYTHON TOOL KIT BY BOHDAN41K")
print("""Select app:
 - Calculator
 - Alert
 - Passwordgen
 - Converter
❗ Write your answer in lower case!""")
selection = input("Write here... ")
if selection == "calculator":
   calc()
elif selection == "alert":
    alert()
elif selection == "passwordgen":
    passgen()
elif selection == "converter":
   converter()