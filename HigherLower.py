from art import higherlower_logo, higherlower_logo2
from higherlowergamedata import game_data
import random
import sys, subprocess

def game_over():
    print("Game over! Your score is : ",score)

def format_data(account):
    return f"{account["name"]} a {account["description"]} from {account["country"]}."

def check_answer(guess, followerA, followerB):
    if followerA > followerB:
        return guess == "a"
    else:
        return guess == "b"

#main
print(higherlower_logo)
score = 0
game = True 
B = random.choice(game_data)
while game == True:
    A = B
    B = random.choice(game_data)
    while A == B:
        B = random.choice(game_data)
    followerA = A["follower_count"]
    followerB = B["follower_count"]
    print(f"Compare A: {format_data(A)}")
    print(higherlower_logo2)
    print(f"Against B: {format_data(B)}")

    #asking
    guess = input("Who has moree followers A or B?: ").lower()
    answer = check_answer(guess, followerA, followerB)
    #clearing screen
    subprocess.run('cls', shell=True)
    print(higherlower_logo)
    if answer == True:
        score += 1
        print(f"Correct! Current score: {score}")
    else:
        print(f"Wrong answer! Your score is {score}")
        game = False
