from art import logo, vs
from game_data import data
import random


def format_data(account):
    account_nam = account["name"]
    account_desc = account["description"]
    account_cou = account["country"]
    return f"{account_nam}, a {account_desc}, from {account_cou}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        if guess == "a":
            return True
    else:
        if guess == 'b':
            return True


print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has the more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You are right! Current score {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score:{score} ")