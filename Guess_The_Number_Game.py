import random

com_num = random.randint(1,20)
max_tries = 5
tries_left = 1
print("Im thinking of a number between 1 and 20. Guess my number:")
while tries_left < max_tries:
    accept = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    try:
        user_num = int(input())
        if user_num not in accept:
            print("That is not a number between 1 and 20.")
            break

        else:
            if user_num == com_num:
                print("Congratulations! You guess correctly!")
                break

            elif user_num > com_num:
                print("That number is too high!", max_tries - tries_left, "attempts left. Try again:")
                tries_left +=1

            elif user_num < com_num:
                print("That number is too Low!", max_tries - tries_left, "attempts left. Try again:")
                tries_left +=1
    except ValueError:
        print ("This is not a number between 1 and 20.")

if tries_left >=5:
    print("You've exceeded your number of guesses for this round.")