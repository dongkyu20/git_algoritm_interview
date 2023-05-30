s = "cbbd"

s = list(s)
result = []
#홀수 팰린드롬
for i in range(len(s)):
    left = i -1
    right = i + 1
    while left >= 0 and right <= len(s) - 1:
        if s[left] == s[right] and len(s[left:right+1]) >= len(result):
            result = s[left:right+1]
            left -= 1
            right += 1
        elif s[left] == s[right]:
            left -= 1
            right += 1
        else:
            break

#짝수 팰린드롬
for i in range(len(s)):
    left = i
    right = i + 1
    while left >= 0 and right <= len(s) - 1:
        if s[left] == s[right] and len(s[left:right + 1]) >= len(result):
            result = s[left:right + 1]
            left -= 1
            right += 1
        elif s[left] == s[right]:
            left -= 1
            right += 1
        else:
            break

if result == []:
    result = list(s)[0]

print(''.join(result))

#교재 풀이

def expand(left: int, right: int) -> str:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

##예외 리턴
if len(s) < 2 or s == s[::-1]:
    return s
result = ''

for i in range(len(s) -1):
    result = max(result, expand(i, i+1), expand(i, i+2),
                 key = len)
return result
