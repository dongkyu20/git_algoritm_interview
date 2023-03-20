nums = [3, 2, 4]
target = 6

'''

리스트 인덱스, 값 저장법

nums_map = {}
for i, num in enumerate(nums):
    nums_map[num] = i




'''

# 포인터 브루트포스 -- 패스


# target - nums[i] --- 1000ms
for i in range(len(nums)):
    if target - nums[i] in nums and nums.index(target - nums[i]) != i:
        print(i, nums.index(target - nums[i]))
        break

def twoSum(self, nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        if target - nums[i] in nums and nums.index(target - nums[i]) != i:
            return i, nums.index(target - nums[i])
            break


