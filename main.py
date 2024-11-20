# Import
from time import sleep
import random
import winsound
from winsound import PlaySound
from random import randint
from datetime import date
from datetime import datetime
import sys
import random
import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas
# Variables

all_symbols = 'abcdefghijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ12345678901@#$%^&*()_-=+;:/?.>'
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
marked_as_done = False
variants = ["rock", "paper", "scissors"]
rps_mode = "None"
available_modes = ["singleplayer", "2 players"]
player1_choice = "None"
player2_choice = "None"
bot_choice = "None"
try_again_choice = "None"
todays_date = date.today().strftime("%B %d, %Y")
now = datetime.now()
current_time = now.strftime("%I:%M %p")
settings_answer = "None"
settings_answer_changes = "None"
apps_pack_version = "1.7-beta1"
random_word_range = []
random_word_input = None
remove_word_input = 0
generated_word = None
# Functions

def calc():
 print("CALCULATOR")
 a = int(input("First num: "))
 b = int(input("Second num: "))
 c = input("Select action: ")
 if c == "+":
    print("The result is...")
    sleep(2)
    print(a + b)
 elif c == "-":
    print("The result is...")
    sleep(2)
    print(a - b)

 elif c == "*":
    print("The result is...")
    sleep(2)
    print(a * b)
 elif c == "/":
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
    global all_symbols
    print("PASSWORD GENERATOR")
    print("")
    print("Please, enter the length of password")
    length = int(input())
    if length < 8:
       print("WARNING! THE PASSWORD IS LESS THAN 8 SYMBOLS! YOUR PASSWORD WILL BE EASIER TO GUESS!")
       password = ''.join(random.choice(all_symbols) for i in range(length))
       print(password)
    elif length >= 100:
      print("The app may crash or console log may be unreadable. Are you sure? (Y/N)")
      length_answ = str.lower(input())
      if length_answ == "y":
        password = ''.join(random.choice(all_symbols) for i in range(length))
        print(f"I generated a reliable password for you: {password}")
      elif length_answ == "n":
        main_menu()
    else:
     password = ''.join(random.choice(all_symbols) for i in range(length))
     print(f"I generated a reliable password for you: {password}")

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
    notesAnswer = str.lower(input())
    for notes in available_notes:
     if notesAnswer == notes:
         print("")
         print(available_notes[notes])
         print("")
         print("Edit | Mark as done | Delete")
         editdeleteansw = str.lower(input("Write here... "))
         if editdeleteansw == "edit":
            available_notes[notes] = input("Write the new note and press Enter... ")
         elif editdeleteansw == "mark as done":
            available_notes[notes] = available_notes[notes] + u' ✓'
         elif editdeleteansw == "delete":
            available_notes[notes] = "None"
    if notesAnswer == "close this app":
      notes_work = False
def singleplayer_mode():
   player1_choice = str.lower(input("Please, enter your choise: rock, paper or scissors... "))
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
   player1_choice = str.lower(input("Player 1, please, enter your choise: rock, paper or scissors... "))
   player2_choice = str.lower(input("Player 2, please, enter your choice: rock, paper or scissors... "))
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
 rps_mode = str.lower(input("Write here... "))
 if rps_mode == available_modes[0]:
     singleplayer_mode()
 elif rps_mode == available_modes[1]:
     two_players_mode()
 else:
     print("Please, enter a valid game mode!")
     sleep(2)
     rock_paper_scissors()
def settings():
 global current_time
 print("""Select option you want to change:
 - Clock mode
 - Information""")
 settings_answer = str.lower(input(""))
 if settings_answer == "clock mode":
   print("Select mode:")
   print("12 hours (AM, PM)")
   print("24 hours")
   settings_answer_changes = str.lower(input())
   if settings_answer_changes == "12 hours" or settings_answer_changes == "12h":
    if current_time != now.strftime("%I:%M %p"):
     current_time = now.strftime("%I:%M %p")
     print("Changes applied!")
     sleep(2)
     main_menu()
    else:
      print("Changes not applied: you already set 12 hours mode")
      sleep(2)
      main_menu()
   if settings_answer_changes == "24 hours" or settings_answer_changes == "24h":
    if current_time != now.strftime("%H:%M"):
     current_time = now.strftime("%H:%M")
     print("Changes applied!")
     sleep(2)
     main_menu()
    else:
      print("Changes not applied: you already set 24 hours mode")
      sleep(2)
      main_menu()
 if settings_answer == "info" or settings_answer == "information":
   print("")
   print("APP INFORMATION")
   print("")
   print(f"Apps pack version: {apps_pack_version}")
   print("")
   print(f"Python interpreter version: {sys.version}")
   print("")
   print("It's an open-source app. You can view the code here - https://github.com/JustBohdan41k/alltheprojects/")
   sleep(2)
   main_menu()
def randomword():
    global random_word_input
    global random_word_range
    def main_gen():
     global random_word_input
     global random_word_range
     global remove_word_input
     global generated_word
     print("")
     print("RANDOM WORD GENERATOR")
     print("Your words list:")
     print("")
     print(", ".join(map(str, random_word_range)))
     if not random_word_range:
         print("It seems, you haven't got any word in your list. Let's add it!")
     print("")
     print("Add | Remove | Clear list | Generate")
     random_word_input = str.lower(input())
     if random_word_input == "add":
         random_word_range.append(input("Enter new word... "))
         main_gen()
     elif random_word_input == "remove":
        if not random_word_range:
          print("")
          print("It seems, you haven't got any word in your list. Let's add it!")
          sleep(2)
          main_gen()
        else:
         print(", ".join(map(str, random_word_range)))
         print("")
         print("Select index of word to remove (first word is number 0)")
         remove_word_input = int(input())
         del random_word_range[remove_word_input]
         main_gen()
     elif random_word_input == "clear list":
         random_word_range.clear()
         main_gen()
     elif random_word_input == "generate":
         if len(random_word_range) < 2:
             print("Can't generate random word: try to add more words!")
             sleep(1.5)
         else:
          generated_word = random.choice(random_word_range)
          print(f"Generated random word: {generated_word}")
          sleep(1.5)
          main_gen()
    main_gen()
def simple_paint():
  root = tk.Tk()
  root.title("Paint")
  root.geometry("600x600")
  canvas = ScrolledCanvas(root)
  canvas.pack(fill=tk.BOTH, expand=True)
  t = RawTurtle(canvas)
  custom_col = t.color("black")
  t.speed(1)
  x, y = t.pos()
  def draw_forward(event=root.bind('d')):
      t.setheading(0)
      t.forward(10)
  root.bind('d', draw_forward)
  def draw_backward(event=root.bind('a')):
      t.setheading(180)
      t.forward(10)
  root.bind('a', draw_backward)
  def draw_up(event=root.bind('w')):
      t.setheading(90)
      t.forward(10)
  root.bind('w', draw_up)
  def draw_forward(event=root.bind('s')):
      t.setheading(270)
      t.forward(10)
  root.bind('s', draw_forward)
  def eraser():
      custom_col = t.color("white")
  def drawing():
      custom_col = t.color("black")
  def black():
     custom_col = t.color("black")
  def red():
     custom_col = t.color("red")
  def orange():
     custom_col = t.color("orange")
  def yellow():
     custom_col = t.color("yellow")
  def green():
     custom_col = t.color("green")
  def cyan():
     custom_col = t.color("cyan")
  def blue():
     custom_col = t.color("blue")
  def purple():
     custom_col = t.color("purple")
  def set_custom_color(event=None):
      color = f"#{custom_col_entry.get()}"
      try:
          t.color(color)
      except tk.TclError:
          print("Invalid color format.")
  er = tk.Button(root, text="Erase", width=9, height=2, command=eraser)
  dr = tk.Button(root, text="Draw", width=9, height=2, command=drawing)
  black = tk.Button(root, text=" ", width=2, height=2, background="black", command=black)
  red = tk.Button(root, text=" ", width=2, height=2, background="red", command=red)
  orange = tk.Button(root, text=" ", width=2, height=2, background="orange", command=orange)
  yellow = tk.Button(root, text=" ", width=2, height=2, background="yellow", command=yellow)
  green = tk.Button(root, text=" ", width=2, height=2, background="green", command=green)
  cyan = tk.Button(root, text=" ", width=2, height=2, background="cyan", command=cyan)
  blue = tk.Button(root, text=" ", width=2, height=2, background="blue", command=blue)
  purple = tk.Button(root, text=" ", width=2, height=2, background="purple", command=purple)
  custom_col_label = tk.Label(root, text="Your own color (HEX):")
  custom_col_entry = tk.Entry(root, width=30)
  custom_col_entry.bind("<Return>", set_custom_color)
  dr.pack(side=tk.LEFT)
  er.pack(side=tk.LEFT)
  black.pack(side=tk.LEFT)
  red.pack(side=tk.LEFT)
  orange.pack(side=tk.LEFT)
  yellow.pack(side=tk.LEFT)
  green.pack(side=tk.LEFT)
  cyan.pack(side=tk.LEFT)
  blue.pack(side=tk.LEFT)
  purple.pack(side=tk.LEFT)
  custom_col_label.pack(side=tk.LEFT)
  custom_col_entry.pack(side=tk.LEFT)
  root.mainloop()
# The main menu

def main_menu():
 print("")
 print(f"PYTHON APPS BY BOHDAN41K | {todays_date}, {current_time}")
 print("")
 print("""Select app:
 - Calculator
 - Alert
 - Passwordgen
 - Converter
 - Random number generator (write 'randomnum')
 - Notes
 - Rock, paper, scissors (write "rps")
 - Random word generator (write "rwg")
 - Simple paint (you can write "sp")
 - Settings
 """)
 selection = str.lower(input("Write here... "))

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
 elif selection == "settings":
   settings()
 elif selection == "rwg":
   randomword()
 elif selection == "simple paint" or selection == "sp":
   simple_paint()
 else:
   print("Please, select the valid app")
   sleep(2)
   main_menu()

#Call main menu when starting code

main_menu()
