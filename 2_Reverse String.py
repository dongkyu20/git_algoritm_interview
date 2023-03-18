s = ["H","a","n","n","a","h"]

def reverseString(self, s:list[str]) -> None:
    left = 0
    right = len(s)-1

    while left < right:
        s[left], s[right] = s[right] , s[left]
        left += 1
        right -= 1


# 내 풀이 리트에서는 틀렸다고 나옴 --> !!!do not allocate another array!!!
# def reverseString(self, s:list[str]) -> None:
#     a = []
#     for i in range(len(s)):
#         a.append(s[len(s)-1-i])
#     s = a

