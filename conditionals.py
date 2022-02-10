# Method to evaluate data
# if then else

import random

high_range = 100
middle_num = int(high_range / 2)
my_guess = middle_num 
number_guesses = 0

my_random_number = random.randrange(1,high_range)
# my_random_number = 42

print (my_random_number)

while True:
    number_guesses +=1
    if my_random_number == my_guess: # evaluate the guess
        print ('You win the mumber was ', my_random_number)
        print ('Number of guesses', number_guesses)
        break
    #------- LESS THAN -------
    elif my_random_number < my_guess:
        
        # Modify the guess to be in the middle of the range
        high_range = my_guess # high range = 50
        my_guess = int(middle_num / 2)
        middle_num = my_guess
    # ------- GREATER THAN -------
    else :
        
        # Modify the guess to be in the middle of the range
        # greater than middle number -- less than high range
        # 50 hr - 25 mn / 2 = 12.5 +25 = 37
        range = (high_range - middle_num)/2 + middle_num
        my_guess = int(range)
        middle_num = my_guess