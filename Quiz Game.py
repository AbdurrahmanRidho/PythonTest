# Abdurrahman Ridho

print ("Welcome to anime quiz!")

play = input("Are you weebs?")

if play.lower() != "yes":
    quit()

print ("Okay! lets start ")
score = 0

# No 1
answer = input("When One Piece first release? ")
if answer.lower() == "1999":
    print('Correct!')
    score += 1
else:
    print("Incorrect")


# No 2
answer = input("Tokyo Ghoul opening 1? ")
if answer.lower() == "unravel":
    print('Correct!')
    score += 1
else:
    print("Incorrect")


# No 3
answer = input("Does One Piece have more than 1000 episodes? ")
if answer.lower() == "yes":
    print('Correct!')
    score += 1
else:
    print("Incorrect")


# No 4
answer = input("Attack on Titan opening 1? ")
if answer.lower() == "guren no yumiya":
    print('Correct!')
    score += 1
else:
    print("Incorrect")


# No 5
answer = input("Bleach total episode? ")
if answer.lower() == "366":
    print('Correct!')
    score += 1
else:
    print("Incorrect")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.") # score / jumlah soal