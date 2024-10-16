# Import
from time import sleep
import random
import winsound
from winsound import PlaySound
from random import randint

# Variables

letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', ';', ':', '/', '?', '.', '>']
num = 0
answer = "None"
result = 0
kelvinInCelsium = 273.15
randomRange = [0, 0]
randomResult = 0
availableNotes = {
    "first": "None",
    "second": "None",
    "third": "None",
    "fourth": "None",
    "fifth": "None"
}
notesAnswer = "None"
editdeleteansw = "None"

# Functions

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
   try:
    print("The result is...")
    sleep(2)
    print(a / b)
   except ZeroDivisionError:
    print("You can't divide by zero!")
   finally:
     print(" ")
 if(c != "+" or c != "-" or c != "*" or c != "/"):
    print("Please, use valid math operators!")
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
def celsiumToKelvin():
  amount = int(input("Enter the amount of ℃ "))
  result = amount + kelvinInCelsium
  print(f"The result is {result}")
def celsiumToFahrenheit():
  amount = int(input("Enter the amount of ℃ "))
  result = amount * 9/5 + 32
  print(f"The result is {result}")
def converter():
   print("CONVERTER")
   answer = input("""
   PLEASE, SELECT THE CONVERTION
   - Miles to km
   - km to miles
   - Celsius to Kelvin
   - Celsius to Fahrenheit
   """)
   if answer == "miles to km":
    miles_to_km()
   if answer == "km to miles":
    km_to_miles()
   if answer == "celsius to kelvin":
     celsiumToKelvin()
   if answer == "celsius to fahrenheit":
     celsiumToFahrenheit()
def randomiser():
  randomRange[0] = int(input("Enter the minimum number: "))
  randomRange[1] = int(input("Enter the maximum number: "))

  print(f"Generating random number from {randomRange[0]} to {randomRange[1]}")
  sleep(3)
  randomResult = random.randint(randomRange[0], randomRange[1])
  print(f"The number is {randomResult}")
def notes():
   notesWork = True
   while notesWork:
    print("NOTES")
    print(f"""Please, select available note:
       - First: {availableNotes["first"]}
       - Second: {availableNotes["second"]}
       - Third: {availableNotes["third"]}
       - Fourth: {availableNotes["fourth"]}
       - Fifth: {availableNotes["fifth"]}
       - Close this app""")
    notesAnswer = input()
    for notes in availableNotes:
     if notesAnswer == notes:
         print("")
         print(availableNotes[notes])
         print("")
         print("Edit | Mark as done | Delete")
         editdeleteansw = input("Write here... ")
         if editdeleteansw == "edit":
            availableNotes[notes] = input("Write the new note and press Enter... ")
         elif editdeleteansw == "mark as done":
            availableNotes[notes] = availableNotes[notes] + u' ✓'
         elif editdeleteansw == "delete":
            availableNotes[notes] = "None"
    if notesAnswer == "close this app":
      notesWork = False

# The main menu

print("PYTHON TOOL KIT BY BOHDAN41K")
print("""Select app:
 - Calculator
 - Alert
 - Passwordgen
 - Converter
 - Random number generator (write 'randomnum')
 - Notes
❗ Write your answer in lower case!""")
selection = input("Write here... ")

# Selections

if selection == "calculator":
   calc()
elif selection == "alert":
    alert()
elif selection == "passwordgen":
    passgen()
elif selection == "converter":
   converter()
elif selection == "randomnum":
   randomiser()
elif selection == "notes":
   notes()
