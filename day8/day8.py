data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(line.strip())

test_data = []
with open("./test.txt", "r") as file:
    for line in file:
        test_data.append(line.strip())

def value(data):
    i, acc = 0, 0
    seen = set()
    while i not in seen and i < len(data):
        if 'acc' in data[i]:
            seen.add(i)
            acc += int(data[i].split()[1])
        if 'jmp' in data[i]:
            seen.add(i)
            i += int(data[i].split()[1])
        else:
            i += 1
    return i, acc

print('***** Test *****')
index, acc = value(test_data)
print(acc)

print('***** Part 1 *****')
index, acc = value(data)
print(acc)

print('***** Part 2 *****')

def find_mistake_ret_acc(data):
    changed = set()
    for i, opp in enumerate(data):
        dd = list(data)
        if 'jmp' in opp:
            dd[i] = 'nop' + dd[i][3:]
        if 'nop' in opp:
            dd[i] = 'jmp' + dd[i][3:]
        
        ret, acc = value(dd)
        if len(data) == ret:
            return acc

        dd = list(test_data)

print("Test:", find_mistake_ret_acc(test_data))
print("Answer on input data:", find_mistake_ret_acc(data))
