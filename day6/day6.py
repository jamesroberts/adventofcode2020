test_data = []
with open("./test.txt", "r") as file:
    for line in file:
        test_data.append(line)

data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(line)

def yes_questions(data):
    group = set()
    totals = []
    data.append('\n') # Handle the last group
    for l in data:
        if l == '\n':
            totals.append(len(group))
            group = set()
        else:
            for c in l.strip():
                group.add(c)

    return sum(totals)

print('***** Test *****')
print(yes_questions(test_data))

print('***** Part 1 *****')
print(yes_questions(data))

print('***** Part 2 *****')
from collections import Counter
def all_yes(data):
    totals = []
    group = []
    data.append('\n') # Handle the last group
    for l in data:
        if l == '\n':
            totals.append(all_same(group))
            group = []
        else:
            group.append(l.strip())

    return sum(totals)

def all_same(group):
    count = 0
    c = Counter()
    for p in group:
        c.update(p)
    for q,a in c.items():
        if a == len(group):
            count += 1
    
    return count 

assert 6 == all_yes(test_data)
print(all_yes(data))