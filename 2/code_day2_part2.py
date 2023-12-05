add = 0
add2 = 0

red = 12
blue = 14
green = 13

import re
with open('input.txt', 'r') as file:
    line = file.readline().rstrip("\n")
    while line != "":

        numbers = re.findall(r'\d+', line)
        id = int(numbers[0]) if numbers else None

        game, sets = line.split(": ")
        rounds = sets.split(";")

        mx_red = 0
        mx_blue = 0
        mx_green = 0

        mins = {"red": 0, "green": 0, "blue": 0}
        maxs = {"red": 12, "green": 13, "blue": 14}

        poss = True
        for round in rounds:
            wrong = False
            r = round.split(",")
            for cubes in r:
                if "red" in cubes:
                    cubes = ''.join(filter(lambda x: x.isdigit(), cubes))
                    if int(cubes) > mx_red: mx_red = int(cubes)
                    if int(cubes) > red:
                        poss = False
                        break
                if "blue" in cubes:
                    cubes = ''.join(filter(lambda x: x.isdigit(), cubes))
                    if int(cubes) > mx_blue: mx_blue = int(cubes)
                    if int(cubes) > blue:
                        poss = False
                        break
                if "green" in cubes:
                    cubes = ''.join(filter(lambda x: x.isdigit(), cubes))
                    if int(cubes) > mx_green: mx_green = int(cubes)
                    if int(cubes) > green:
                        poss = False
                        break

        mult = mx_red*mx_blue*mx_green
        add2 += mult

        if poss:
            add += int(id)


        line = file.readline().rstrip("\n")

print(add) #2265
print(add2) #64097