import csv
import random

def solve(lst):
    max_length = 0  # max length of positive number sequence
    current_length = 0

    for i in lst:
        if i > 0:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0

    max_length = max(max_length, current_length)
    print(max_length)

# testing a solve function
'''arr = [random.randint(-30, 30) for i in range(10)]
print(arr)
solve(arr)'''

with open("numbers.csv", 'r', encoding='cp1251') as file:
    reader = csv.reader(file)
    next(reader)

    lst = []
    for row in reader:
        lst.append(int(row[0]))

    solve(lst)



