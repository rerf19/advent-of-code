add = 0

with open('input.txt', 'r') as file:
    line = file.readline().rstrip("\n")
    while line != "":
        table = {
            '1': 'one',
            '2': 'two',
            '3': 'three',
            '4': 'four',
            '5': 'five',
            '6': 'six',
            '7': 'seven',
            '8': 'eight',
            '9': 'nine'
        }

        for key in table:
            line = line.replace(table[key], key)

        # Remove all alphabetic characters
        line = ''.join(filter(lambda x: x.isdigit(), line))

        n = len(line)

        line = line[0] + line[n - 1]
        add += int(line)

        line = file.readline().rstrip("\n")

print("Final Result: " + str(add)) #55686