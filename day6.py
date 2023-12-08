# Day 6

import numpy as np

file = open('./data/day6-data.txt', 'r')
lines = file.readlines()
file.close()

test_data = ["Time:      7  15   30",
             "Distance:  9  40  200"]

# part 1
def tidy_lines_1(lines):
    lines = [line.strip().split() for line in lines]
    [line.pop(0) for line in lines]
    lines = [[int(l) for l in line] for line in lines]
    pairs = np.column_stack(lines)

    return pairs

def beat_the_record_1(pair):
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

def get_answer_1(lines):
    games = tidy_lines_1(lines)
    answer = 1
    
    for game in games:
        ways = beat_the_record_1(game)
        answer *= ways
        print("number of ways:", ways)

    return answer

# part 2
def tidy_lines_2(lines):
    lines = [line.strip() for line in lines]
    lines = [line[line.find(": ") + 1:] for line in lines]
    lines = [line.replace(" ", "") for line in lines]
    lines = [int(line) for line in lines]
    return lines

def beat_the_record_2(pair):
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

def get_answer_2(lines):
    game = tidy_lines_2(lines)
    ways = beat_the_record_2(game)
    return ways


#print("answer 1:", get_answer_1(lines))
print("answer 2:", get_answer_2(lines))