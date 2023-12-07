# Day 5
# Task 1: use the maps to figure out a location number for each seed

file = open('./data/day5-data.txt', 'r')
lines = file.readlines()
file.close()

test_data = ["seeds: 79 14 55 13",
             "",
             "seed-to-soil map:",
             "50 98 2",
             "52 50 48",
             "",
             "soil-to-fertilizer map:",
             "0 15 37",
             "37 52 2",
             "39 0 15",
             "",
             "fertilizer-to-water map:",
             "49 53 8", # 53-60
             "0 11 42", # 11-52
             "42 0 7",
             "57 7 4",
             "",
             "water-to-light map:",
             "88 18 7",
             "18 25 70",
             "",
             "light-to-temperature map:",
             "45 77 23",
             "81 45 19",
             "68 64 13",
             "",
             "temperature-to-humidity map:",
             "0 69 1",
             "1 0 69",
             "",
             "humidity-to-location map:",
             "60 56 37",
             "56 93 4"]

def tidy_lines(lines):
    lines = [line.strip() for line in lines]
    seeds = lines.pop(0).split()
    seeds.pop(0) 
    lines.append(lines.pop(0)) # move the empty string before the first map to the end of the list
    tidy_lines = []
    map = []

    # each map is a [[list of [lists]] within a list]
    for line in lines:
        if line == '':
            tidy_lines.append(map)
            map = []
        else:
            map.append(line)
    
    tidy_lines = [[map.split() for map in line[1:]] for line in tidy_lines]

    return seeds, tidy_lines

def find_location(seed, maps):
    # if source number in source range:
    source = seed
    for map in maps:
        for range in map:
            dest_range_start = int(range[0])
            source_range_start = int(range[1])
            range_length = int(range[2])
                
            if not source_range_start <= source < (source_range_start + range_length):
                continue
            else:
                # get matching destination number
                destination = source - source_range_start + dest_range_start
                # destination number becomes source for next round
                source = destination
                break

    # location is the final source number
    return source

seeds, maps = tidy_lines(lines)

locations = []

for seed in seeds:
    seed = int(seed)
    location = find_location(seed, maps)
    locations.append(location)
    #print(seed, location)

# get smallest location number
locations.sort()
print(locations[0])

