data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(line)

def num_trees(data, right, down):
    i, pos, trees = 0, 0, 0
    while i < len(data) - 1:
        i += down
        p = data[i].strip()
        pos += right
        if pos >= len(p) - 1:
            pos = pos - len(p)
         
        if p[pos] == "#":
            trees += 1
    
    return trees

a = num_trees(data, right=1, down=1)
b = num_trees(data, right=3, down=1)
c = num_trees(data, right=5, down=1)
d = num_trees(data, right=7, down=1)
e = num_trees(data, right=1, down=2)

print(a,b,c,d,e)
print(a*b*c*d*e)