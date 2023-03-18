# 내 풀이
# isalnum, lower 참고

def isPalindrome(self, s:str) -> bool:

    # 영어와 숫자만 입력
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬
    last = len(strs) - 1
    first = 0
    while first <= last:
        if strs[first] == strs[last]:
            first += 1
            last -= 1
        else:
            return False
    if first > last:
        return True







