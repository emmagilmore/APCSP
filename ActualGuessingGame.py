print("welcome to the number guessing game!")

print("how to play: I have chosen four numbers in a specific order.")
print("you are going to guess different four digit numbers until you guess the four digit number I chose.")
print("I will tell you if your guess contains the right number(s) and whether or not they are in the right order.")
print("ready to play?")

import random
randoNumber = random.randint(1000, 9999)
print(randoNumber) #make it not print later
list1 = [int(x) for x in str(randoNumber)]
print(list1) #don't print later

for i in range(0,1000):
    userInput1 = input("your guess: ")
    if len(userInput1) < 4:
        print("remember: your guess can only be four numbers!")
    elif len(userInput1) > 4:
        print("remember: your guess can only be four numbers!")
    else:
        print("your guess is a four digit number, perfect!")
        list2 = [int(x) for x in str(userInput1)]
        print(list2) #don't print later
        for eachlet in list1:
            for everylet in list2:
                if eachlet == everylet:
                    print(list2.index(eachlet))
                else:
                    print("nope")

for eachlet in list1:
    for everylet in list2:
        if eachlet == everylet:
            print(list2.index(eachlet))
        else:
            print("nope")




print("the answer is:")
print(randoNumber)
