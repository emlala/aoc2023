# Day 2
# Task 1: Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. 
# What is the sum of the IDs of those games?
# Task 2: What is the fewest number of cubes of each color that could have been in the bag to make the game possible?
# What is the sum of the power of these sets?

import re

file1 = open('./data/day2-data.txt', 'r')
lines = file1.readlines()
file1.close()

test_data = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", 
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", 
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red", 
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red", 
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

def tidy_line(line):
    line = line.strip()
    new_beginning = line.find(": ")
    id = line[:new_beginning]
    id = re.sub("[^0-9]", "", id)
    line = line[new_beginning + 2:]
    line = line.split("; ")
    line = [round.split(", ") for round in line]
    return id, line

def is_possible_1(line):
    red_max = 12
    green_max = 13
    blue_max = 14
    red = 0
    green = 0
    blue = 0

    for round in line:
        for colour in round: 
            colour = colour.split()

            if colour[1] == "red":
                if int(colour[0]) > red:
                    red = int(colour[0])
                if red > red_max:
                    return False
            if colour[1] == "green":
                if int(colour[0]) > green:
                    green = int(colour[0])
                if green > green_max:
                    return False
            if colour[1] == "blue":
                if int(colour[0]) > blue:
                    blue = int(colour[0])
                if blue > blue_max:
                    return False
                
    return True

def is_possible_2(line):
    red = 0
    green = 0
    blue = 0

    for round in line:
        for colour in round: 
            colour = colour.split()

            if colour[1] == "red":
                if int(colour[0]) > red:
                    red = int(colour[0])
            if colour[1] == "green":
                if int(colour[0]) > green:
                    green = int(colour[0])
            if colour[1] == "blue":
                if int(colour[0]) > blue:
                    blue = int(colour[0])
                
    return red, green, blue


def get_answer_1(lines):
    sum = 0
    for line in lines:
        id, line = tidy_line(line)
        if is_possible_1(line):
            sum += int(id)
    return sum

def get_answer_2(lines):
    power = 0
    sum = 0

    for line in lines:
        id, line = tidy_line(line)
        red, green, blue = is_possible_2(line)
        power = int(red) * int(green) * int(blue) 
        sum += power
    
    return sum

print(get_answer_1(lines))
print(get_answer_2(lines))