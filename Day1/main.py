file = open('input.txt')
data = {}
sumOfElf = 0
index = 0
for line in file:
    if line != "\n":
        sumOfElf += int(line)
    else:
        data[index] = sumOfElf
        sumOfElf = 0
        index += 1
file.close()
ans = sorted(data.items(), key=lambda x: x[1], reverse=True)

def part1(): 
    print(f"The #{ans[0][0]+1}th Elf carried the most Caleries: {ans[0][1]}")

def part2():
    sumOfCalories = 0
    for i in range(0,3):
        sumOfCalories += ans[i][1]
    print(f"The top 3 Elfs carried Calorries in total: {sumOfCalories}")

part1()
part2()
