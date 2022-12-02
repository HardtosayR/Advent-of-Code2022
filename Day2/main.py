file = open('Day2\input.txt')
map = {'X':1, 'Y':2, 'Z':3}
winScore = 6
drawScore = 3
lossScore = 0
map2 = {'A':{'win':'Y','draw':'X','loss':'Z'},
        'B':{'win':'Z','draw':'Y','loss':'X'},
        'C':{'win':'X','draw':'Z','loss':'Y'}
        }

def part1():
    sumOfScore = 0
    for line in file:
        me = line[2]
        Elf = line[0]
        if Elf == 'A' and me == 'X' or Elf == 'B' and me == 'Y' or Elf == 'C' and me == 'Z':
            sumOfScore += map[me] + drawScore
        elif Elf == 'B' and me == 'X' or Elf == 'C' and me == 'Y' or Elf == 'A' and me == 'Z':
            sumOfScore += map[me] + lossScore
        else:
            sumOfScore += map[me] + winScore
    print(f"Total Score of first strategy: {sumOfScore}")

def part2():
    sumOfScore = 0
    for line in file:
        me = line[2]
        Elf = line[0]
        if me == 'X':
            sumOfScore += lossScore + map[map2[Elf]['loss']]
        elif me == 'Y':
            sumOfScore += drawScore + map[map2[Elf]['draw']]
        elif me == 'Z':
            sumOfScore += winScore + map[map2[Elf]['win']]
    print(f"Total score of second strategy: {sumOfScore}")
