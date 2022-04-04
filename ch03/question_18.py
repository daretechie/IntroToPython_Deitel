# TODO: 18 (Challenge: Nested Looping) Modify your script from Exercise 3.17 to display all four patterns
#  side-by-side (as shown above) by making clever use of nested for loops. Separate each triangle from the next by
#  three horizontal spaces. [Hint: One for loop should control the row number. Its nested for loops should calculate
#  from the row number the appropriate number of asterisks and spaces for each of the four patterns.]
#  (a)     (b)    (c)     (d)
#  * ********** ********** *
#  ** ********* ********* **
#  *** ******** ******** ***
#  **** ******* ******* ****
#  ***** ****** ****** *****
#  ****** ***** ***** ******
#  ******* **** **** *******
#  ******** *** *** ********
#  ********* ** ** *********
#  ********** * * **********


print(f'(a){"(b)":>8}{"(c)":>12}{"(d)":>9}')

for row in range(1, 11):
    for _ in range(row):
        print("*", end='')
    print(end="   ")
    for _ in range(11, row, -1):
        print("*", end='')
    print(end="   ")
    for _ in range(11, row, -1):
        print("*", end='')
    print(end="   ")
    for _ in range(row):
        print("*", end="")
    print()

