nums = [1,2,3,4,0]
zero_index = []
result = 1


for i in range(len(nums)):
    if nums[i] != 0:
        result = result * nums[i]
    else:
        zero_index.append(i)

res_lst = []

if len(zero_index) == 1: # case1) 0이 1개
    for i in range(len(nums)):
        if i in zero_index:
            res_lst.append(result)
        else:
            res_lst.append(0)
elif len(zero_index) >= 2: # case2) 0이 2개
    for i in range(len(nums)):
        res_lst.append(0)
else:
    for i in range(len(nums)):
        res_lst.append(result//nums[i])

print(res_lst)


