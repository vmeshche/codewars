def solution(s):
    res = []
    if len(s) % 2:
        s += "_"
    for i in range(0, len(s), 2):
        res.append(s[i:i+2])
    return res


if __name__ == "__main__":
    print(solution("abc"))