class Solution:
    def pushDominoes(self, dominoes):
        res, l, r , pre_l, pre_r = "", {}, {}, None, None,
        for i, s in enumerate(dominoes):
            if s == "." and pre_r != None: r[i] = i - pre_r
            elif s == "R": pre_r = i
            elif s == "L": pre_r = None
        for i in range(len(dominoes) - 1, -1, -1):
            if dominoes[i] == "." and pre_l != None: l[i] = pre_l - i
            elif dominoes[i] == "L": pre_l = i
            elif dominoes[i] == "R": pre_l = None
        for i, s in enumerate(dominoes):
            if s == "L" or s == "R": res += s
            elif i in l and i in r:
                if l[i] < r[i]: res += "L"
                elif r[i] < l[i]: res += "R"
                else: res += s
            elif i in l: res += "L"
            elif i in r: res += "R"
            else: res += s
        return res