# TODO: (Separating the Digits in an Integer) In Exercise 2.11, you wrote a
#  script that separated a five-digit integer into its individual digits and
#  displayed them. Reimplement your script to use a loop that in each
#  iteration “picks off” one digit (left to right) using the // and % operators,
#  then displays that digit.


print("Separating the Digits in an Integer\n")
digits = input('Enter five digit: ')

if len(digits) == 5:
    for i in range(5, 0, -1):
        digits = int(digits)
        digit = digits // 10 ** (i - 1) % 10
        print(digit, end=" ")

else:
    print("Only five digit numbers is allowed")


