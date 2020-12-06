from collections import Counter

data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(line)

# Part 1
def valid_password_count(data):
    valid_passwords = 0
    for i in data:
        min, max = int(i.split()[0].split('-')[0]), int(i.split()[0].split('-')[1])
        char, password = i.split()[1][0], i.split()[2]
        
        counts = Counter(password)
        if counts[char] >= min and counts[char] <= max:
            valid_passwords += 1

    return valid_passwords

print(valid_password_count(data))

# Part 2
def valid_password_count2(data):
    valid_passwords = 0
    for i in data:
        pos1, pos2 = int(i.split()[0].split('-')[0]), int(i.split()[0].split('-')[1])
        char, password = i.split()[1][0], i.split()[2]
        
        if password[pos1-1] == char and password[pos2-1] == char:
            continue
        elif password[pos1-1] == char:
            valid_passwords += 1
        elif password[pos2-1] == char:
            valid_passwords += 1
 
    return valid_passwords

print(valid_password_count2(data))


