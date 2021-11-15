# TODO: 12 (Palindromes) A palindrome is a number, word or text phrase that
#  reads the same backwards or forwards. For example, each of the following
#  five-digit integers is a palindrome: 12321, 55555, 45554 and 11611. Write
#  a script that reads in a five-digit integer and determines whether it’s a
#  palindrome. [Hint: Use the // and % operators to separate the number into
#  its digits.]

print("Palindrome")
digits = input("Enter five digits: ")
digits_list = []
if len(digits) == 5:
    for i in range(5, 0, -1):
        digits = int(digits)
        digit = digits // 10 ** (i - 1) % 10
        digits_list.append(digit)
    if digits_list[0] == digits_list[4] and digits_list[1] == digits_list[3]:
        print("This is a Palindrome digit")
    else:
        print("This is not a Palindrome digit")
else:
    print("Only five digits are allowed")