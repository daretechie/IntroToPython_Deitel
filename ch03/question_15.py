# TODO: 15 (Challenge: Approximating the Mathematical Constant e) Write a
#  script that estimates the value of the mathematical constant e by using the
#  formula below. Your script can stop after summing 10 terms.
#  e = 1 + 1/1! + 1/2! + 1/3!


first_number = 1
e_value = 0
denominator = 1
numerator = 1

for i in range(1, 11):
    denominator *= i
    e_value += first_number + numerator / denominator
    print(e_value)
