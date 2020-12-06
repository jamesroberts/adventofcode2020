data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(line)

def extract_passports(data):
    passports = []
    p = {}
    # Cover last passport in list
    data.append('\n')
    for l in data:
        if l == '\n':
            passports.append(p)
            p = {}

        details = l.split()
        for d in details: 
            k, v = d.split(":")
            p[k] = v

    return passports

pp = extract_passports(data)

def count_valid(passports):
    count = 0
    valid_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for pp in passports:
        if all(k in pp.keys() for k in valid_keys):
            if valid_fields(pp):
                count += 1

    return count 

import re
def valid_fields(passport):
    try:
        for k, v in passport.items():
            if k == 'byr':
                if (int(v) > 2002) or (int(v) < 1920): return False
            if k == 'iyr':
                if (int(v) < 2010) or (int(v) > 2020): return False
            if k == 'eyr':
                if (int(v) < 2020) or (int(v) > 2030): return False
            if k == 'hgt':
                hgt, unit = int(v[:-2]), v[-2:]
                if (unit == 'cm' and (hgt < 150 or hgt > 193)): return False
                if (unit == 'in' and (hgt < 59 or hgt > 76)): return False
            if k == 'hcl':
                citeria = re.compile(r'^#[0-9a-f]{6}$')
                if not (citeria.match(v)): return False
            if k == 'ecl':
                if v not in ['amb','blu','brn','gry','grn','hzl','oth']: return False
            if k == 'pid':
                citeria = re.compile(r'^[0-9]{9}$')
                if not citeria.match(v): return False

        return True

    except ValueError as err: 
        return False


print(count_valid(pp))           