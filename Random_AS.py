import random

words = ["Gossip Girl","One Tree Hill","Glee","Friends","Gilmore Girls"]
hint1 = ["Ed Westick stars in it","Sophia Bush stars in it","Chris Colfer stars in it","Lisa Kudrow stars in it","Lauren Graham stars in it"]
hint2 = ["They live in the Upper East Side", "They live in North Carolina", "They live in Ohio", "They live in West Village", "They live in Connecticut"]

number = random.randint(0,4)

secretword = words[number]

guess = ""

counter = 0
         
while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'length', 'first letter', 'last letter', or 'give up' if you need help.")
    guess = input()

    if counter > 4:
        print("Too many guesses!")

    elif guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break
    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "length":
        print( len(secretword) )

    elif guess == "first letter":
        print( secretword[0] )

    elif guess == "last letter":
        print( secretword[-1] )

    elif guess == "give up":
        print( "The secret word was " + secretword )
        break
    else:
        print("Try again.")
        counter += 1
        
        
        
        
         
