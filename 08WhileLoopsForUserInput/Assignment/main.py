import random

# number = random.randint(1,10)
# is_incorrect = True

# while is_incorrect:
#     response = int(input("enter your guess"))
#     if response > number:
#         print("response is too high")
#     elif response < number:   
#         print("response is too low")
#     elif response == number:
#         is_incorrect = False
#         print("Correct!")

# number = random.randint(1,10)
# lives = 2
# is_incorrect = True
# while is_incorrect:
#     response = int(input("enter your guess "))
#     if response > number and lives > 0:
#         lives = lives - 1
#         print("response is too high", lives )
#     elif response < number and lives > 0:
#         lives = lives - 1
#         print("response is too low", lives )
#     elif lives == 0:
#         print("Game over")
#         is_incorrect = False
#     else:
#         print("correct!")
#         is_incorrect = False
number = 50
print(number)
Total = True
while Total == True:
    amount_entered = int(input("enter your coin amount between (10, 25, or 5) "))
    if amount_entered != 10 and amount_entered != 5 and amount_entered != 25:
        print("invalid amount entered")
        Total = False
    elif number > 0:
        amount_entered == 10 or amount_entered == 5 or amount_entered == 25
        Total = True
        sub_amount = number - amount_entered
        number = sub_amount
        print(number)
    else:
        number == 0
        Total = False 
        print("Total due paid")



