import random

my_random_number = random.randrange(1,20)

my_first_number = 42
my_second_number = 30.5

print(type(my_first_number))
print(type(my_second_number))
print(type(my_random_number))

total = my_first_number + my_second_number
print(total)
print(type(total))

print('My random number is',my_random_number) # cast an alternate datatype