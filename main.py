#If we list all the numbers between 1 and 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# Add those numbers together and you get 23.
# Find the sum of all the numbers between 1 and 1000 that are multiples of 3 or 5.


sum_of_numbers_multiples_3_and_5 = 0
for number in range(1000):
    if number % 3 == 0 and number % 5 == 0:
        sum_of_numbers_multiples_3_and_5 = sum_of_numbers_multiples_3_and_5 + number
    elif number % 5 != 0 and number % 3 == 0:
        sum_of_numbers_multiples_3_and_5 = sum_of_numbers_multiples_3_and_5 + number
    elif number % 5 == 0:
        sum_of_numbers_multiples_3_and_5 = sum_of_numbers_multiples_3_and_5 + number
print(sum_of_numbers_multiples_3_and_5)
