"""Using nested control statements to analyze examination results."""

# initialize variables
passes = 0  # number of passes
failures = 0  # number of failures

result = int(input('Enter result (1=pass, 2=fail) and -1 to end: '))

while result != -1:
    # print("Oops! 1 and 2 Only")
    if result == 1:
        passes += 1
    elif result == 2:
        failures += 1

    result = int(input('Enter result (1=pass, 2=fail) and -1 to end: '))

# termination phase
print('Passed:', passes)
print('Failed:', failures)

if passes > 8:
    print('Bonus to instructor')
