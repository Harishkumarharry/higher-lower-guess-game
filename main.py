from game_data import data
import random
from art import logo, vs
from os import system
# from replit import clear

def get_random_data():
    return random.choice(data)

def formatting_data(choice):
    name = choice['name']
    description = choice['description']
    country = choice['country']
    return f"{name}, a {description}, from {country}"

def compare(user_guess, a_followers, b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def game():
    should_continue = True
    score = 0
    a_choice = get_random_data()
    b_choice = get_random_data()

    while should_continue:
        a_choice = b_choice
        b_choice = get_random_data()

        while a_choice == b_choice:
            b_choice = get_random_data()

        print(f"Compare A: {formatting_data(a_choice)}")
        print(vs)
        print(f"Compare B: {formatting_data(b_choice)}")

        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_ans = compare(user_guess, a_followers=a_choice['follower_count'], b_followers=b_choice['follower_count'])

        system('cls')
        # clear()
        print(logo)
        if correct_ans:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            should_continue = False
            print(f"Sorry, that's wrong. Final Score: {score}.")

game()