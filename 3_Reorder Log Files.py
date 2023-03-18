logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def reorderLogFiles(self, logs: list[str]) -> list[str]:
    # 문자 숫자 확인 및 분류
    for i in range(len(logs)):
        logs[i] = logs[i].split()
    logsal = []
    logsnum = []
    for i in range(len(logs)):
        if ''.join(logs[i][1:]).isnumeric():
            logsnum.append(logs[i])
        else:
            logsal.append(logs[i])

    logsal = sorted(logsal, key = lambda x : (x[1:], x[0]))
    logs = logsal + logsnum

    for i in range(len(logs)):
        logs[i] = " ".join(logs[i])

