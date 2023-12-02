
add = 0

with open('input.txt', 'r') as file:
    line = file.readline().rstrip("\n")
    while line != "":
        print("Original Line:  " + line)

        # Remove all alphabetic characters
        line = ''.join(filter(lambda x: not x.isalpha(), line)) 
        
        print("Remove Alphabetic Characters:  " + line)

        n = len(line)

        if n == 1:
            line = line + line
            print("n=1: " + line)
            add = add + int(line)
        else:
            line = line[0] + line[n-1]
            print("n!=1: " + line)
            add = add + int(line)

        #New Line
        line = file.readline().rstrip("\n")

print("Final Result: " + str(add))

        
