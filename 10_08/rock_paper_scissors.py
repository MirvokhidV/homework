import random


def game_decorator(func):
    def wrapper():
        print("Print starting game...")
        func()
        print("Game over")
    return wrapper


@game_decorator
def game():
    score = {
        'user': 0,
        'pc': 0
    }
    for i in range(int(input("How many times do you want to play: "))):
        print(
            f"\nScore: \n\tUser: {score.get('user', 0)}\n\tComputer: {score.get('pc', 0)}")
        while True:
            user_choice = input("\nChoose rock, paper, or scissors: ")
            if user_choice not in ["rock", "paper", "scissors"]:
                print("Invalid choice. Please try again.")
            else:
                break
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"Computer chose {computer_choice}.")
        if user_choice == computer_choice:
            print(f"It's a tie in {i+1}'s turn!")
            score['user'] += 1
            score['pc'] += 1
        elif ((user_choice == "rock" and computer_choice == "scissors")
              or (user_choice == "paper" and computer_choice == "rock")
              or (user_choice == "scissors" and computer_choice == "paper")):
            print(f"You win in {i+1}'s turn!")
            score['user'] += 1
        else:
            print(f"Computer wins in {i+1}'s turn!")
            score['pc'] += 1

    print("***************----Overall----***************")
    if score.get('user', 0) > score.get('pc', 0):
        print("\nCongratulations you winned!")
    elif score.get('user', 0) < score.get('pc', 0):
        print("\nFOOOO! You are failed, computer winned")
    elif score.get('user', 0) == score.get('pc', 0):
        print("It's tile")
    print(
        f"\nOverall score is: \n\t\t\tUser: {score.get('user', 0)}\n\t\t\tComputer: {score.get('pc', 0)}")
    input()


if __name__ == '__main__':
    game()
