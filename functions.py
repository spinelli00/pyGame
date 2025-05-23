from random import randint, choice
from sys import exit
from os import system
from time import sleep
score: int = 0


def clear_display():
    sleep(1)
    system('cls')

def sum_custom():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    result = num1 + num2
    print(f"{num1} + {num2} = ?")
    return result

def subtraction():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    result = num1 - num2
    print(f"{num1} - {num2} = ?")
    return result

def multiplication():
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    result = num1 * num2
    print(f"{num1} * {num2} = ?")
    return result

def user_insert():
    while True:
        try:
            user_result = int(input("Insert the result >> "))
            return user_result
        except ValueError:
            print("Invalid input, try again!")

def validation(correct_result, user_result):
    global score
    if user_result == correct_result:
        print("Correct!")
        score += 1
        print(f'Your Score : {score}')
    else:
        print(f"Wrong! The correct answer was {correct_result}.")

def niveleasy():
    operation = choice([sum_custom, subtraction])
    correct_result = operation()
    user_result = user_insert()
    validation(correct_result, user_result)
    continue_game()

def nivelhard():
    operation = choice([sum_custom, subtraction, multiplication])
    correct_result = operation()
    user_result = user_insert()
    validation(correct_result, user_result)
    continue_game()

def continue_game():
    while True :
        try :
            option1 = int(input("Do you wanna continue (1. Yes | 2. No) >> "))
            if option1 == 1 :
                print("Okay, Lets Start Again !")
                clear_display()
                break
            elif option1 == 2 :
                print("Okay, Getting out ... ")
                clear_display()
                exit()
            else : 
                print("Invalid option, Try Again !")
                clear_display()
        except ValueError :
            print("Invalid option, Try Again !")
            clear_display()
