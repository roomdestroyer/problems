# 进行 n 局游戏，连赢 k 局的概率为 p=(1/2)^(k+1)*(n-k+2)，本程序为枚举验证公式的工具
def getnext(s):
    n = [0] * len(s)
    j = -1
    n[0] = -1
    for i in range(1, len(s)):
        while s[j + 1] != s[i] and j != -1:  # 一定要先回退
            j = n[j]
        if s[j + 1] == s[i]:  # 再判断相等
            n[i] = j + 1
        j = n[i]
    return n


def kmp(text, pattern, nex):
    n = len(text)
    m = len(pattern)
    j = -1
    for i in range(n):
        while text[i] != pattern[j + 1] and j != -1:  # 一定要先回退
            j = nex[j]
        if text[i] == pattern[j + 1]:  # 再判断相等
            j += 1
        if j == m - 1:
            return j
    return False


if __name__ == '__main__':
    pattern = "11111"
    n = 10
    oldp = 0
    newp = 0
    while True:
        cnt = 0
        for i in range(1 << int(n)):
            s = ""
            for j in range(int(n)):
                if i & (1 << j):
                    s += "1"
                else:
                    s += "0"
            nex = getnext(pattern)
            if kmp(s, pattern, nex):
                cnt = cnt + 1
            oldp = newp
            newp = cnt / (2 ** int(n))
        print("n = ", n, "  ", cnt / (2 ** int(n)), "    ", newp - oldp)
        n = n + 1

