# Day 4
# Task 1: Figure out which of the numbers you have (right) appear in the list of winning numbers (left). 
# The first match makes the card worth one point and each match after the first doubles the point value of that card.
# Task 2: Points only cause you to win more cards equal to the number of winning numbers you have.
# You win copies of the scratchcards below the winning card equal to the number of matches. Continue processing, including the copies. 
# Count the final total number of cards

file = open('./data/day4-data.txt', 'r')
lines = file.readlines()
file.close()

test_data = ["Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
             "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
             "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
             "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
             "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
             "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"]

def tidy_lines(lines):
    lines = [line[line.find(": ") + 2:] for line in lines]
    lines = [line.split(" | ") for line in lines]
    lines = [[[numbers.split() for numbers in line]] for line in lines]
    return lines

def check_matches(line):
    winning_numbers = line[0]
    played_numbers = line[1]
    matches = []

    for num in winning_numbers:
        if num in played_numbers:
            matches.append(num)
    return(matches)

def calculate_points(matches):
    count = len(matches) - 1
    points = 1
    return points * 2 ** count

def get_result(lines):
    lines = tidy_lines(lines)
    # sum = 0
    card_count = 0

    for index, line in enumerate(lines):
        for card in line:
            card_count += 1
            matches = check_matches(card)
            copies = len(matches)
            if copies > 0:
                # add a copy to as many of the following lines as is the value of match_count
                while copies > 0:
                    copy = lines[index+copies][0]
                    lines[index+copies].append(copy)
                    copies -= 1
                # points = calculate_points(matches)
                # sum += points

    return card_count

print(get_result(lines))