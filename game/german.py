# todo - Create the dictionary and get a random word
# Create a Dictionary that can be used as a database. Keys for Mother language, Values Target Language.

language_practice = {"Book":"Buch"}

#Variables for the game.
## Start with 10 Lives
## At floor 1
## Strak start at 0, and goes back to 0 each misspelling word
lives = 10
floor = 1
streak = 0

# Here is the game logic
## While loop, that while the lives are greater than 0, the game runs.
while lives > 0:
    #just printing the greating message, it is outside the input and if statement, therefore it plays every time.
    print(f"Hello, you at at floor {floor}, with {lives} lives good luck climbing it, I believe in you!!!")
    if streak % 3 == 0 and streak != 0:
        #Here the streak NEEDS to be before the elif statement, Python reads line by line in a if statement.
        #That means if it satisfy this condition, it will not read the other ones
        #This if statement, simple increase lives by 1, every time the streak is mutiple of 3.
        lives += 1
        print(f"Congratulations, your streak is {streak}, you get a life bonus now you have {lives} lives")

    elif streak > 0:
        #Just a simple encorage message for every streak greater than 0, but only if is not mutiple of 3
        print(f"You have {streak} streak, wow, you are on fire!!")

    else:
        #Just a print for everytime the streak is 0, not needed the f-string, but just for future growth
        print(f"Your streak is 0, but don't give up!!")
    #All the code above, runs BEFORE this, eliminating problems for multiple if for diferent variables.
    #Input storage in a variable, it returns a string, whatch out for wanted integers formats, not in this case.
    answer = input(f"What is the german word for {language_practice.keys()}?: ")
    #TODO - still not aplied the random word generator, just using the one to verify the logic of the game first.
    if answer != language_practice["Book"]:
        #this code increases the lives lost by 1 each 10 floor, because the "//" only returns the integer part
        #that means bellow 10, returns 0, 10-19, returns 1 and so on.
        lives -= (floor//10) + 1
        #everytime a word is misspelled, restart the streak to 0.
        streak = 0
        print("Wrong, Lost a life")
    elif answer == language_practice["Book"]:
        print("Good job, climbed a floor")
        #increases the floor by 1
        floor +=1
        #increases the streak by 1
        streak += 1
    else:
        #This is not necessary, cuz the answer or is equal or diferent, but I decided to use a escape loop.
        #IDK why, but in case something happens, it is a learning opportunity
        print("This should not be happening")

else:
    #this happens when the while loop ends, lives bellow 1, so it means game over.
    #TODO - in the future I can add a ranking system, to compare the highest floor achieved.
    #Could be a DB, or simple as a List, storing the floor info, and then using a max function.
    #Needed to use another file though, maybe a dictionary, with name and floor.
    #Than using list(dicionary.keys(), or .values()), than using max value, IDK, not gonna do it right now.
    print(f"You lost, but you reached floor {floor}")