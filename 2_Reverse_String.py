class Solution:
    # reverse 활용
    # def reverseString(self, s: list[str]) -> None:
    #     s.reverse()
    def reverseString(self,s : list[str])-> None:
        a = []
        for i in range(len(s)):
            a.append(s[len(s)-1-i])
        s = a
