data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(int(line))

def findAns1(data):
    target = 2020
    for i in data:
        if target - i in data:
            return i, target - i

a, b = findAns1(data)
print(a, b)
print(a*b)

def findAns2(data):
    target = 2020
    for i in data:
        second_target = target - i
        for x in data:
            if second_target - x in data:
                return x, second_target -x, i

a, b, c = findAns2(data)
print(a, b, c)
print(a*b*c)




