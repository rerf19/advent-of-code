
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

s = 0

for l,r in zip(left_column,right_column):
    diff = l - r
    s = s + abs(diff)

print(s)