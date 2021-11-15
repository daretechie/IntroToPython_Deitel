# TODO: 14 (Challenge: Approximating the Mathematical Constant π) Write a
#  script that computes the value of π from the following infinite series. Print
#  a table that shows the value of π approximated by one term of this series,
#  by two terms, by three terms, and so on. How many terms of this series do
#  you have to use before you first get 3.14? 3.141? 3.1415? 3.14159?
#  π = 4 - 4/3 + 4/5 - 4/7 .........

max_pie_value = [3.14, 3.141, 3.1415, 3.14159]
pie_value = 0
denominator = 1.0
first_term = 4
max_term = 200000

print(f'{"":>2}Terms{"PI Values":>18}')
for i in range(1, max_term + 1):
    for r in range(1, 6):
        new_pie_value = round(pie_value, r)
        if new_pie_value in max_pie_value:
            print(f'{i:>6} {new_pie_value:>17}')
            max_pie_value.remove(new_pie_value)
    if i % 2 != 0:
        pie_value += first_term / denominator
    else:
        pie_value -= first_term / denominator
        # print(f'{i:>2}{pie_value:>20.5f}')
    denominator += 2.0
