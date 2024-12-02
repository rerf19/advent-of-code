
with open("input.txt", "r") as file:
    lines = file.readlines()

left_column = []
right_column = []

for line in lines:
    left, right = map(int, line.split())
    left_column.append(left)
    right_column.append(right)

left_column.sort()
right_column.sort()

sim = 0
s= 0

for l in left_column:
    for r in right_column:
        if l == r:
            sim = sim + 1
        s = s +(l * sim)
        sim = 0

print(s)