# TODO: 19 (Brute-Force Computing: Pythagorean Triples) A right triangle can have sides that are all integers. The
#  set of three integer values for the sides of a right triangle is called a Pythagorean triple. These three sides
#  must satisfy the relationship that the sum of the squares of two of the sides is equal to the square of the
#  hypotenuse. Find all Pythagorean triples for side1, side2 and hypotenuse (such as 3, 4 and 5) all no larger than
#  20. Use a triple-nested for-loop that tries all possibilities. This is an example of “brute-force” computing.
#  You’ll learn in more advanced computer science courses that there are many interesting problems for which there is
#  no known algorithmic approach other than sheer brute force.

x, y, z = 1, 1, 1

print(f'{"Side1":>2} {"side2":>10} {"hypotenuse":>15} {"total":>8}')
for x in range(1, 21):
    X = x ** 2
    for y in range(1, 21):
        Y = y ** 2
        for z in range(1, 21):
            Z = z ** 2
            if Z == (Y + X):
                print(f'{x:>3} {y:>10} {z:>12} {Z:>12}')
print()
