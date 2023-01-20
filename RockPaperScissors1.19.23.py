import random

def askToPlay():
    print("Welcome to the Game");
play = input("We're going to play Rock, Paper, Scissors. Cool? ")
answers = ["yes", "Yes", "yea", "Yea", "ok", "Ok", "OK", "Y", "y"]

if play in answers:
    print("OK, lets count it out..")
    continue

def nowPlaying():
    userWeapon = ("rock", "paper", "scissors")
    player = None
    computer = random.choice(options)

    player = input("Rock, Paper, Scissors, SHOOT!: ")

print(f"Player: {player}")
print(f"Computer: {computer}")

askToPlay()
nowPlaying()