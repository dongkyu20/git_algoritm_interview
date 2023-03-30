nums = [-4, -3, -2, -1, -1, 0, 0, 1, 2, 3, 4]


#내 풀이  __타임아웃__
nums = sorted(nums)
result = []

left = 0
right = len(nums) - 1
for i in range(len(nums)):
    while left < i:
        if -(nums[left] + nums[i]) in nums[i+1:right+1]:
            result.append([nums[left], nums[i], -(nums[left] + nums[i])])
            left += 1
        elif -(nums[left] + nums[i]) < nums[right] and right > i+1:
            right -= 1
        else:
            left += 1

    left = 0
    right = len(nums)-1

print(right)
check = []
for i in range(len(result)):
    if result[i] not in result[i+1:]:
        check.append(result[i])
    else:
        result[i] = []


print(check)
