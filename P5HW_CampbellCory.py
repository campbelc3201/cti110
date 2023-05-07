# Welcome to Math Quiz
# 4May2023
# CTI-110 P5HW - Math Quiz
# Cory Campbell


import random
def Addition():
    a = random.randint(1,100)
    b = random.randint(1,100)
    print("   ",a)
    print(" + ",b)
    sum = a+b
    answer = int(input("\nEnter answer: "))
    guess = 1
    while sum!=answer:
        if answer<sum:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")
        answer = int(input("\ntry again: "))
        guess+=1
    print("Congratulations!!!! your answer is correct....")
    print("Number of guesses: ",guess)

def Subtraction():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print("   ", a)
    print(" - ", b)
    diff = a - b
    answer = int(input("\nEnter answer: "))
    guess = 1
    while diff != answer:
        if answer < diff:
            print("Sorry, guess is too low.")
        else:
            print("Sorry, guess is too high.")
        answer = int(input("\ntry again: "))
        guess += 1
    print("Congratulations!!!! your answer is correct....")
    print("Number of guesses: ", guess)

def main():
    print("\nMain Menu")
    print("-"*15)
    print("1. Addition Random Numbers")
    print("2. Subtraction Random Numbers")
    print("3. Exit\n")
    option = int(input("Please choose one of the option: "))
    if option==1:
        Addition()
    elif option==2:
        Subtraction()
    elif option == 3:
        print("Thank you for playing..")
        print("Bye!!")
        exit()
    else:
        print("Invalid option. Please choose again")
    main()


print("Welcome to the Math Quiz\n")
main()
