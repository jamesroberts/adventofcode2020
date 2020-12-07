data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(line)

print("***** Part 1 *****")
def find_bags(data, bag, bags):
    for l in data:
        f,r = l.split("bags contain")
        if bag in r:
            if f not in bags:
                bags.add(f)
                find_bags(data, f, bags)
    return bags

ans = find_bags(data, "shiny gold", set())
print("Number of bags:", len(ans))


print("***** Part 2 *****")
def find_nested_bags(data, bag):
    for l in data:
        f, r = l.split("bags contain")
        if bag in f:
            count = 0
            for n in r.split(','):
                nn = n.strip().split()[0]
                if nn.isnumeric():
                    new_bag = " ".join(n.strip().split()[1:3])
                    count += int(nn) + (int(nn) * find_nested_bags(data, new_bag))

            return count

print("Nested bags:", find_nested_bags(data, "shiny gold"))

