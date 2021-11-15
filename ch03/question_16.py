# TODO: 16 (Nested Control Statements) Use a loop to find the two largest values
#  of 10 numbers entered.

number = []

for num in range(1, 11):
    number_input = int(input(f"Enter number {num}: "))
    number.append(number_input)

max_value = number[0]
max_value_2nd = number[0]
for value in number:
    if value > max_value:
        max_value = value
    if value > max_value:
        if max_value < max_value_2nd:
            max_value_2nd = value
            # max_value_2nd = max(max_value_2nd, value)

print(f'\nThe largest are {max_value} and {max_value_2nd}')
