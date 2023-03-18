import re
from collections import Counter
"""
설계 실수 문자열 타입에서 소문자 치환, 금지 단어 삭제, 구두점 삭제하려 했으나
굳이 그렇게 할 필요 없었음
어차피 단어 카운트 하려면 리스트로 전환되어야 함
"""
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

# 변수명 설정 연습? 경험? 필요할 듯

def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
    paragraph = paragraph.lower()
    paragraph = re.sub(r'[^1-9a-z\s]', '', paragraph)
    paragraph = paragraph.split()
    paragraph1 = []
    for i in range(len(paragraph)):
        if paragraph[i] not in banned:
            paragraph1.append(paragraph[i])

    p_counter = Counter(paragraph1)
    return p_counter.most_common(n=1)[0][0]
