

def getInfo(line):
    game, numbers = line.split(":")
    winning_nums, nums = numbers.split("|")
    return game,winning_nums,nums

def checkHowManyWinnigNumbers(winning_nums, nums):
    win_n = list(filter(None, winning_nums.split(" ")))
    n = list(filter(None, nums.strip().split(" ")))
    
    number_of_winning_cards = 0
    
    for i in range(len(n)):
        if n[i] in win_n:
            number_of_winning_cards +=1
    
    return number_of_winning_cards

    print("----")


points = 0 

with open('input.txt', 'r') as file:
        for line in file.readlines():
            game, winning_nums, nums = getInfo(line)
            
            n = checkHowManyWinnigNumbers(winning_nums,nums)

            if n > 0:
                points += 2 ** (n - 1)

print(points) #23750
#p2 = 13261850

