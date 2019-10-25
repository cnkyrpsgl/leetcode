class Solution:
    def splitIntoFibonacci(self, S):
        def getStarter():
            arr = []
            for i in range(1, len(S) - 1):
                for j in range(i + 1, len(S)):
                    s1, s2 = S[:i], S[i:j]
                    if (s1[0] == "0" and len(s1) > 1) or (s2[0] == "0" and len(s2) > 1): 
                        continue
                    arr.append((int(s1), int(s2), j))
            return arr                 
        def dfs(arr, i):
            if i == len(S):
                return arr
            sm = arr[-2] + arr[-1]
            l = len(str(sm))
            new = int(S[i:i + l])
            return new == sm and 0 <= sm <= mx and dfs(arr + [new], i + l)
        q, mx = getStarter(), 2 ** 31 - 1
        for p1, p2, i in q:
            seq = dfs([p1, p2], i)
            if seq:
                return seq
        return []