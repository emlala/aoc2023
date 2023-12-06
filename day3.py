# Day 3
# Task 1: Any number adjacent to a symbol, even diagonally, is a "part number". What is the sum of all of the part numbers?
# Task 2: Asterisk (*) with two connected numbers is a gear. What is the sum of the gear numbers multiplied?

file1 = open('./data/day3-data.txt', 'r')
lines = file1.readlines()
file1.close()

test_data = ["467..114..", 
             "...*......", 
             "..35..633.", 
             "...633#...", 
             "617*......", 
             ".....+.586", 
             "..592.....", 
             "......755.", 
             "...$.*....", 
             ".664.598..",]

def tidy_lines(lines):
    lines = [line.strip() for line in lines]
    lines = [list(line) for line in lines]
    empty_row = ["."] * len(lines[0])
    lines.insert(0, empty_row)  
    lines.insert(len(lines), empty_row)
    return lines

def list_neighbours(char_index, line_index, last_in_line):
    if last_in_line == True:
        neighbour_list = [[line_index - 1, char_index - 1], [line_index - 1, char_index], 
                          [line_index, char_index - 1], 
                          [line_index + 1, char_index - 1], [line_index + 1, char_index]]
        return neighbour_list
    else:
        neighbour_list = [[line_index - 1, char_index - 1], [line_index - 1, char_index], [line_index - 1, char_index + 1], 
                          [line_index, char_index - 1], [line_index, char_index + 1], 
                          [line_index + 1, char_index - 1], [line_index + 1, char_index], [line_index + 1, char_index + 1]]
        return neighbour_list

def is_symbol(char):
    if char != "." and char.isnumeric() == False:
        return True
    else:
        return False

def find_whole_number(index, line):
    number = line[index]
    original_index = index
    while index > 0 :
        if line[index - 1].isnumeric():
            index -= 1
            number = line[index] + number
            line[index] = "."
        else:
            break

    index = original_index

    while index < len(line) - 1:
        if line[index + 1].isnumeric():
            index += 1
            number = number + line[index]
            line[index] = "."
        else:
            break

    return int(number)

def is_part_number(char_index, line_index, lines):
    line = lines[line_index]

    if line[char_index].isnumeric():

        if char_index == len(line) - 1:
            neighbours = list_neighbours(char_index, line_index, True) 
        else:
            neighbours = list_neighbours(char_index, line_index, False)

        for y, x in neighbours:
            if is_symbol(lines[y][x]):
                return True  
            else:
                return False
    else: 
        return False
    
def get_gear_nums(char_index, line_index, lines):
    line = lines[line_index]
    part_numbers = []
    
    if line[char_index] == "*":
        if char_index == len(line) - 1:
            neighbours = list_neighbours(char_index, line_index, True)
        else:
            neighbours = list_neighbours(char_index, line_index, False)
        
        for y, x in neighbours:
            if lines[y][x].isnumeric():
                whole_number = find_whole_number(x, lines[y])
                part_numbers.append(whole_number)
        
    if len(part_numbers) == 2:
        return part_numbers
    else:
        return None

    


def get_sum(lines): 
    lines = tidy_lines(lines)
    # sum_1 = 0
    gear_ratio_sum = 0
    gears = []

    for line_index, line in enumerate(lines):
        if line_index == 0 or line_index == len(lines) - 1:
            continue
        for char_index, char in enumerate(line):
            # part 1 - find numbers connected to a symbol
            # if is_part_number(char_index, line_index, lines):
            #     whole_number = find_whole_number(char_index, line)
            #     sum_1 += whole_number
            
            # part 2 - find *'s connected to two numbers
            gear = get_gear_nums(char_index, line_index, lines)
            if gear != None:
                gears.append(gear)

    for g in gears:
        gear_ratio = g[0] * g[1]
        gear_ratio_sum += gear_ratio
    
    return gear_ratio_sum

print(get_sum(lines))
