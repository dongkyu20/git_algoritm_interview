height = [0,2,0]

# 내 풀이. 실패

'''
def starter(list = height):
        if height[i] > 0:
            return i
    for i in range(len(height)):
            break
    else:
        return 0


first_index = starter(height)
max_height = height[first_index]
max_index = first_index

def trapping(height, first_index, max_height, T):
    rain = 0
    for i in range(first_index, len(height) - 1):
        T = 1
        if height[i + 1] >= max_height and first_index - i > 1 :
            print(i, first_index)
            rain += (i - first_index) * max_height - sum(height[first_index + 1:i + 1])
            max_height = height[i + 1]
            first_index = i + 1
        elif i == len(height) - 2 and height[i] != max_height:
            T += 1
            print(T)
            print(max(height[first_index+T:]), first_index)
            rain += trapping(height, first_index, max(height[first_index+T:]),T)
    return rain

print(trapping(height, first_index, max_height, T))


for i in range(first_index, len(height)-1):
    if height[i+1] >= max_height and max_index - i != 0:
        print(i+1, max_index, max_height)
        rain += (i - max_index) * max_height - sum(height[max_index+1:i+1])
        print(rain)
        max_height = height[i + 1]
        max_index = i + 1
'''

# 교재 풀이
'''
if not height:
    print(0)

volume = 0
left, right = 0, len(height) - 1
left_max, right_max = height[left] , height[right]

while left < right:
    left_max, right_max = max(height[left], left_max), max(height[right], right_max)

    if left_max <= right_max:
        volume += left_max - height[left]
        left += 1
    else:
        volume += right_max - height[right]
        right -= 1

print(volume)

'''


# 교재 풀이 보고 내 풀이 다시

if not height:
    print(0)

left, right = 0, len(height) - 1
height_max = max(height)
index = 0
for i in height:
    if i > 0:
        left = index
        break
    else:
        index += 1
index = len(height)-1
for i in height[::-1]:
    if i > 0:
        right = index
        break
    else:
        index -= 1

left_first = left
right_last = right
left_max, right_max = height[left], height[right]

while left_max != height_max:
    left += 1
    left_max = height[left]


while right_max != height_max:
    right -= 1
    right_max = height[right]

volume = 0

num = 0
left_max = height[left_first]
for i in range(left_first, left+1):
    if i == left_first:
        pass
    elif left_max >= height[i]: # 벽이 낮아지거나 같다
        num += 1
    else: # 벽이 높아지면
        volume += num * left_max - sum(height[left_first+1:i])
        num = 0
        left_first = i
        left_max = height[i]

num = 0
right_max = height[right_last]

if right != len(height) - 1:
    for i in range(right_last, right-1, -1):
        if i == right_last:
            pass
        elif right_max >= height[i]:
            num += 1
        else:
            volume += num * right_max - sum(height[i+1:right_last])
            num = 0
            right_last = i
            right_max = height[i]
if left != right:
    volume += height_max * (right - left - 1) - sum(height[left+1:right])

print('volume = ' , volume)


















def trap(self, height: list[int]) -> int:
    print(1)