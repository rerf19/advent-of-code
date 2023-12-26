add = 0
import re
with open('test.txt', 'r') as file:
    line = file.readline().rstrip("\n")
    while line != "":
        
        numbers = re.findall(r'\d+', line)
        id = int(numbers[0]) if numbers else None

        game, sets = line.split(": ")
        rounds = sets.split(";")

        red = 12
        blue = 14
        green = 13

        poss = True
        for round in rounds:
            print(round)
            r = round.split(",")
            for cubes in r:
                print("new" + str(cubes))
                if "red" in cubes:
                    cubes = ''.join(filter(lambda x: x.isdigit(), cubes))
                    if int(cubes) > red:
                        #print('red' + str(cubes))
                        poss = False
                        break
                if "blue" in cubes:
                    cubes = ''.join(filter(lambda x: x.isdigit(), cubes))
                    if int(cubes) > blue:
                        #print('blue' + str(cubes))
                        poss = False
                        break
                if "green" in cubes:
                    cubes = ''.join(filter(lambda x: x.isdigit(), cubes))
                    if int(cubes) > green:
                        #print('green' + str(cubes))
                        poss = False
                        break

        if poss:
            add += int(id)


        line = file.readline().rstrip("\n")

print(add)