# Day 1
# Task 1: On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.
# Task 2: Spelled out numbers must be taken into account as well.

import re

file1 = open('./data/data-1-1.txt', 'r')
lines = file1.readlines()
file1.close()

test_data = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen', 'sevendxbninefour2fourclmln', 'fourfourfourfourfour']
total_sum = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


for line in lines:
    for index, n in enumerate(numbers):
        indices = [m.start() for m in re.finditer(n, line)]
        if indices:
            for i_index, i in enumerate(indices):
                i = i + 2 + i_index
                line = line[:i] + str(index + 1) + line[i:]
    
    line = re.sub("[^0-9]", "", line)
    line = line[0] + line[-1]
    total_sum += int(line)

print(total_sum)
