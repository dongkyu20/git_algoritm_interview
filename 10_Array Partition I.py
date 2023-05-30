nums = [1,4,3,2]

nums.sort()
key = 0

for i in range(len(nums)):
    if nums[i] < 0:
        key = i

