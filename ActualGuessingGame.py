print("welcome to the number guessing game!")

print("how to play: I have chosen four numbers in a specific order.")
print("you are going to guess different four digit numbers until you guess the four digit number I chose.")
print("I will tell you if your guess contains the right number(s) and whether or not they are in the right order.")
print("ready to play?")
print("     ")

import random
randoNumber = random.randint(1000, 9999)
print(randoNumber) #make it not print later
list1 = [int(x) for x in str(randoNumber)]
print(list1) #don't print later

usersuccess =["_", "_", "_", "_"]

guesses = 10

while guesses != 0:
    userInput1 = input("your guess: ")
    if len(userInput1) < 4:
        print("remember: your guess can only be four numbers!")
        guesses = guesses - 1
    elif len(userInput1) > 4:
        print("remember: your guess can only be four numbers!")
        guesses = guesses - 1
    else:
        list2 = [int(x) for x in str(userInput1)]
        print(list2) #don't print later
        if int(userInput1) == randoNumber:
            print("nice job! you guessed my four digit number correctly!")
        else:
            print("your guess is a four digit number, perfect!")
            for eachlet in list1:
                for everylet in list2:
                    if eachlet == everylet:
                        if list1.index(eachlet) == list2.index(everylet):
                            usersuccess.insert(list2.index(everylet), list2[list1.index(eachlet)])
                            usersuccess.pop(list2.index(everylet) + 1)
                        else:
                            print("the number in the", list2.index(eachlet) + 1, "spot is in the answer but it is not in the right spot.")
                            print("     ")

            print("this is your progress so far!")
            print(usersuccess)
            print("     ")

if guesses < 0:
    print("you ran out of guesses...good try!")
    print("the answer is:")
    print(randoNumber)
