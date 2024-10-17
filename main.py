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
kelvin_in_celsium = 273.15
random_range = [0, 0]
random_result = 0
available_notes = {
    "first": "None",
    "second": "None",
    "third": "None",
    "fourth": "None",
    "fifth": "None"
}
notes_answer = "None"
edit_delete_answer = "None"
variants = ["rock", "paper", "scissors"]
rps_mode = "None"
available_modes = ["singleplayer", "2 players"]
player1_choice = "None"
player2_choice = "None"
bot_choice = "None"
try_again_choice = "None"

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
 elif(c == "-"):
    print("The result is...")
    sleep(2)
    print(a - b)

 elif(c == "*"):
    print("The result is...")
    sleep(2)
    print(a * b)
 elif(c == "/"):
   try:
    print("The result is...")
    sleep(2)
    print(a / b)
   except ZeroDivisionError:
    print("You can't divide by zero!")
   finally:
     print(" ")
 else:
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
def celsium_to_kelvin():
  amount = int(input("Enter the amount of ℃ "))
  result = amount + kelvin_in_celsium
  print(f"The result is {result}")
def celsium_to_fahrenheit():
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
     celsium_to_kelvin()
   if answer == "celsius to fahrenheit":
     celsium_to_fahrenheit()
def randomiser():
  random_range[0] = int(input("Enter the minimum number: "))
  random_range[1] = int(input("Enter the maximum number: "))

  print(f"Generating random number from {random_range[0]} to {random_range[1]}")
  sleep(3)
  randomResult = random.randint(random_range[0], random_range[1])
  print(f"The number is {randomResult}")
def notes():
   notes_work = True
   while notes_work:
    print("NOTES")
    print(f"""Please, select available note:
       - First: {available_notes["first"]}
       - Second: {available_notes["second"]}
       - Third: {available_notes["third"]}
       - Fourth: {available_notes["fourth"]}
       - Fifth: {available_notes["fifth"]}
       - Close this app""")
    notesAnswer = input()
    for notes in available_notes:
     if notesAnswer == notes:
         print("")
         print(available_notes[notes])
         print("")
         print("Edit | Mark as done | Delete")
         editdeleteansw = input("Write here... ")
         if editdeleteansw == "edit":
            available_notes[notes] = input("Write the new note and press Enter... ")
         elif editdeleteansw == "mark as done":
            available_notes[notes] = available_notes[notes] + u' ✓'
         elif editdeleteansw == "delete":
            available_notes[notes] = "None"
    if notesAnswer == "close this app":
      notes_work = False
def singleplayer_mode():
   player1_choice = input("Please, enter your choise: rock, paper or scissors... ")
   bot_choice = random.choice(variants)
   print("")
   print("Your choice: " + player1_choice)
   print("Bot's choice: " + bot_choice)
   if player1_choice == "rock" and bot_choice == "scissors":
       print("")
       print("Rock beats scissors! You won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice == "scissors" and bot_choice == "rock":
       print("")
       print("Rock beats scissors! You lost! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice == "paper" and bot_choice == "rock":
       print("")
       print("Paper beats rock! You won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice == "rock" and bot_choice == "paper":
       print("")
       print("Paper beats rock! You lost! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice == "scissors" and bot_choice == "paper":
       print("")
       print("Scissors beat paper! You won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice == "paper" and bot_choice == "scissors":
       print("")
       print("Scissors beat paper! You lost! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice == "rock" and bot_choice == "rock":
       print("")
       print("It's tie! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice == "paper" and bot_choice == "paper":
       print("")
       print("It's tie! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice == "scissors" and bot_choice == "scissors":
       print("")
       print("It's tie! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        singleplayer_mode()
       else:
        main_menu()
   elif player1_choice != "rock" or player1_choice != "paper" or player1_choice != "scissors":
       print("")
       print("Please, enter rock, paper or scissors!")
def two_players_mode():
   player1_choice = input("Player 1, please, enter your choise: rock, paper or scissors... ")
   player2_choice = input("Player 2, please, enter your choice: rock, paper or scissors... ")
   print("")
   print("Player 1's choice: " + player1_choice)
   print("Player 2's choice: " + player2_choice)
   if player1_choice == "rock" and player2_choice == "scissors":
       print("")
       print("Rock beats scissors! Player 1 won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice == "scissors" and player2_choice == "rock":
       print("")
       print("Rock beats scissors! Player 2 won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice == "paper" and player2_choice == "rock":
       print("")
       print("Paper beats rock! Player 1 won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice == "rock" and player2_choice == "paper":
       print("")
       print("Paper beats rock! Player 2 won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice == "scissors" and player2_choice == "paper":
       print("")
       print("Scissors beat paper! Player 1 won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice == "paper" and player2_choice == "scissors":
       print("")
       print("Scissors beat paper! Player 2 won! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice == "rock" and player2_choice == "rock":
       print("")
       print("It's tie! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice == "paper" and player2_choice == "paper":
       print("")
       print("It's tie! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice == "scissors" and player2_choice == "scissors":
       print("")
       print("It's tie! Try again? (Y/N)")
       try_again_choice = input()
       if try_again_choice == "Y" or try_again_choice == "y":
        two_players_mode()
       else:
        main_menu()
   elif player1_choice != "rock" or player1_choice != "paper" or player1_choice != "scissors" or player2_choice != "rock" or player2_choice != "paper" or player2_choice != "scissors":
       print("")
       print("Please, enter rock, paper or scissors!")
def rock_paper_scissors():
 print("")
 print("ROCK-PAPER-SCISSORS")
 print("")
 print("""Select the mode:
 - Singleplayer (with bot)
 - 2 players""")
 print("")
 rps_mode = input("Write here... ")
 if rps_mode == available_modes[0]:
     singleplayer_mode()
 elif rps_mode == available_modes[1]:
     two_players_mode()
 else:
     print("Please, enter a valid game mode!")
# The main menu

def main_menu():
 print("")
 print("PYTHON TOOL KIT BY BOHDAN41K")
 print("")
 print("""Select app:
 - Calculator
 - Alert
 - Passwordgen
 - Converter
 - Random number generator (write 'randomnum')
 - Notes
 - Rock, paper, scissors (write "rps")
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
 elif selection == "rps":
   rock_paper_scissors()
 else:
   print("Please, select the valid app")

#Call main menu when starting code

main_menu()
