# Day 6

import numpy as np

file = open('./data/day6-data.txt', 'r')
lines = file.readlines()
file.close()

test_data = ["Time:      7  15   30",
             "Distance:  9  40  200"]

def tidy_lines(lines):
    lines = [line.strip().split() for line in lines]
    [line.pop(0) for line in lines]
    lines = [[int(l) for l in line] for line in lines]
    pairs = np.column_stack(lines)

def beat_the_record(pair):
    time = pair[0]
    record = pair[1]
    number_of_ways = 0
    button = 0

    while button <= time:
        time_left = time - button
        distance = button * time_left
        if distance > record:
            number_of_ways += 1
        button += 1

    return number_of_ways

games = tidy_lines(lines)
answer = 1
for game in games:
    ways = beat_the_record(game)
    answer *= ways
    print("number of ways:", ways)

print("answer:", answer)