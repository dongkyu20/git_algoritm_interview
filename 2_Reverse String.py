

# 내 풀이 리트에서는 틀렸다고 나옴
def reverseString(self, s:list[str]) -> None:
    a = []
    for i in range(len(s)):
        a.append(s[len(s)-1-i])

    s = a

# 포인터나 reverse 메서드 사용
