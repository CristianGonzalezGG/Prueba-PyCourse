#rock paper siccorss
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("Welcome to the classic Game Rock Paper Scissors")
while True:
    chooseOne = int(input("""3.. 2.. 1.. CHOOSE ONE
    1(ROCK) 2(PAPER) 3(SCISSORS)
    """))
    print("YOUR CHOOSE:  ")

    if chooseOne == 1:
        print(rock)
    elif chooseOne == 2:
        print(paper)
    elif chooseOne == 3:
        print(scissors)

    print("THE COMPUTER SELECTED: ")
        
    randomInteger = random.randint(1,3)
    if randomInteger == 1:
        print(rock)
    elif randomInteger == 2:
        print(paper)
    elif randomInteger == 3:
        print(scissors)
        
    if chooseOne == 1 and randomInteger == 1:
        print("IT'S A DRAW")
    elif chooseOne == 1 and randomInteger == 3:
        print("YOU WIN!!")
    elif chooseOne == 1 and randomInteger == 2:
        print("YOU LOSE!! :(")
    elif chooseOne == 2 and randomInteger == 2:
        print("IT'S A DRAW")
    elif chooseOne == 2 and randomInteger == 1:
        print("YOU WIN!!")
    elif chooseOne == 2 and randomInteger == 3:
        print("YOU LOSE!! :(")
    elif chooseOne == 3 and randomInteger == 3:
        print("IT'S A DRAW")
    elif chooseOne == 3 and randomInteger == 2:
        print("YOU WIN!!")
    elif chooseOne == 3 and randomInteger == 1:
        print("YOU LOSE!! :(")
    option = input("U wanna Play again")
    if option == "n":
        break
    