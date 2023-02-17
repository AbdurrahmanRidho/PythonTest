# Abdurrahman Ridho
import random

user_wins = 0
computer_wins = 0

options = ["semut", "manusia", "gajah"]

while True:
    user_input = input("Type semut / manusia / gajah or Q to quit :").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # semut : 0, manusia : 1, gajah : 2
    computer_pick = options [random_number]
    print("Komputer Memilih", computer_pick + ".")

    if user_input == "semut" and computer_pick == "gajah":
        print("Kamu Menang!")
        user_wins += 1

    elif user_input == "manusia" and computer_pick == "semut":
        print("Kamu Menang!")
        user_wins += 1

    elif user_input == "gajah" and computer_pick == "manusia":
        print("Kamu Menang!")
        user_wins += 1

    else:
        print("Kamu Kalah!")
        computer_wins += 1

print("Kamu Menang", user_wins, "times.")
print("Komputer Menang", computer_wins, "times.")
print("Thanks, Goodbye!")