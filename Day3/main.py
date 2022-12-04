def findDouble(x:str)->int:
    length = len(x) - 1
    index1 = length // 2 - 1
    index2 = length // 2
    x = tuple(x)
    while index1 != -1:
        s = slice(index2,length)
        ch = x[s]
        if x[index1] in ch:
            if x[index1].islower():
                return ord(x[index1])-ord('a')+1
            else:
                return ord(x[index1])-ord('A')+27
        index1 -= 1
            
def findTriple(x:str, y:str, z:str)->int:
    temp = []
    temp.append(x)
    temp.append(y)
    temp.append(z)
    minLengthStr = min(temp,key=len)
    temp.remove(minLengthStr)
    for i in minLengthStr:
        if i in temp[0] and i in temp[1]:
            if i.islower():
                return ord(i)-ord('a')+1
            else:
                return ord(i)-ord('A')+27

def part1():
    ans = list()
    file = open('input.txt')
    for line in file:
        temp=findDouble(line)
        ans.append(temp)

    file.close()
    print(f"The sum of those items priority is: {sum(ans)}")



def part2():
    index = 0
    temp = list()
    data = list()
    file = open('input.txt')
    for line in file:
        temp.append(line)
        index += 1
        if index == 3:
            data.append(findTriple(temp[0],temp[1],temp[2]))
            temp = []
            index = 0
    print(f"The sum of those items priority is: {sum(data)}")