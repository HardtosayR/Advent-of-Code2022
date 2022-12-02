f = open('input.txt')
data = {}
sum = 0
index = 0
for line in f:
    if line != "\n":
        sum += int(line)
    else:
        data[index] = sum
        sum = 0
        index += 1
f.close()
maxvalue = 0
ans = 0
for i in data.keys():
    if data[i] >= maxvalue:
        maxvalue = data[i]
        ans = i+1

print(f"The {ans}th Elf carries the most Calories: {data[ans]}")