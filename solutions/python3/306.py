class Solution:
    def isAdditiveNumber(self, num):
        def getStarter():
            arr = []
            for i in range(1, len(num) - 1):
                for j in range(i + 1, len(num)):
                    s1, s2 = num[:i], num[i:j]
                    if (s1[0] == "0" and len(s1) > 1) or (s2[0] == "0" and len(s2) > 1): 
                        continue
                    arr.append((int(s1), int(s2), j))
            return arr                 
        def dfs(pre1, pre2, i):
            if i == len(num):
                return True
            sm = pre1 + pre2
            l = len(str(sm))
            new = int(num[i:i + l])
            return new == sm and dfs(pre2, new, i + l)
        q = getStarter()
        return any(dfs(p1, p2, i) for p1, p2, i in q)