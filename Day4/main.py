def isContain(line:str)->bool:
    temp = line.strip('\n')
    temp = temp.split(',')
    temp[0] = temp[0].split('-')
    temp[1] = temp[1].split('-')
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i][j] = int(temp[i][j])
    
    if temp[0][0] >= temp[1][0] and temp[0][1] <= temp[1][1]:
        return True
    elif temp[0][0] <= temp[1][0] and temp[0][1] >= temp[1][1]:
        return True
    else:
        return False

def isOverlap(line:str)->bool:
    temp = line.strip('\n')
    temp = temp.split(',')
    temp[0] = temp[0].split('-')
    temp[1] = temp[1].split('-')
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            temp[i][j] = int(temp[i][j])
    if temp[0][0] > temp[1][1]:
        return False
    elif temp[0][1] < temp[1][0]:
        return False
    else:
        return True

def part1():
    ans = 0
    file = open('input.txt')
    for line in file:
        if isContain(line):
            ans += 1
    print(f"The number of fully contained pairs: {ans}")

def part2():
    ans = 0
    file = open('input.txt')
    for line in file:
        if isOverlap(line):
            ans += 1
    print(f"The number of overlapped pairs: {ans}")
