data = []
with open("./input.txt", "r") as file:
    for line in file:
        data.append(line.strip())

test_data = []
with open("./test.txt", "r") as file:
    for line in file:
        test_data.append(line.strip())

def value(data, preamble):
    queue = []
    for l in data:
        if len(queue) < preamble:
            queue.append(int(l))
        else:
            # print(queue, l)
            in_queue = False
            for n in queue:
                comp = int(l) - n
                if comp < 0:
                    comp = n - int(l)
                if comp in queue and comp != n:
                    in_queue = True
                    # print(l, n, comp)
                    break
            
            if not in_queue:
                return int(l)
    
            queue.pop(0)
            queue.append(int(l))

   
print('***** Test *****')
ans = value(test_data, 5)
print(ans)

print('***** Part 1 *****')
err_num = value(data, 25)
print(err_num)

print('***** Part 2 *****')
def encryption_weakness(data, err_num):
    nums = []
    for i in data:
        # print(nums)
        if sum(nums) == err_num:
            return min(nums) + max(nums)
 
        nums.append(int(i))
        while sum(nums) > err_num:
            nums.pop(0)
            

print("Test:", encryption_weakness(test_data, 127))
print("Answer on input data:", encryption_weakness(data, err_num))
