# TODO: 13 (Factorials) Factorial calculations are common in probability. The
#  factorial of a non-negative integer n is written n! (pronounced “n factorial”)
#  and is defined as follows:
#  n! = n · (n - 1) · (n - 2) · … · 1
#  for values of n greater than or equal to 1, with 0! defined to be 1. So,
#  5! = 5 · 4 · 3 · 2 · 1
#  which is 120. Factorials increase in size very rapidly. Write a script that
#  inputs a non-negative integer and computes and displays its factorial. Try
#  your script on the integers 10, 20, 30 and even larger values. Did you find
#  any integer input for which Python could not produce an integer factorial
#  value?

n = int(input("Enter number to find the factorial: "))
total = 1
if n >= 0:
    for i in range(n, 0, -1):
        total *= i
    print("The factorial value of", n, "!is", total)
