import random
number=random.randint(1,100)
def intro():
    print("may i ask your name?")
    global name 
    name=input()
    print(name,"we are going to play a game number guessing game.I am thinking of a number between 1 to 100.")
    if number %2==0:
        x="even"
    else:
            x="odd"
    print("the number is ",x)
def pic():
    gt=0
    while gt<6:
        guess=int("Enter your number")
        if guess<=100 and guess>=1:
            gt+=1
            if gt<6:
                if guess<number:
                    print("your number is too low")
                if guess >number:
                    print("your number is too hige")
                if guess !=number:
                    print("try again")
                if guess==number:        
                            break