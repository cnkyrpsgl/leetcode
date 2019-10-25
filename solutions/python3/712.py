class Solution:
    def minimumDeleteSum(self, s1, s2):
        l1, l2 = len(s1) + 1, len(s2) + 1
        d = [[0] * l2 for i in range(l1)]
        for i in range(l1):
            for j in range(l2):
                c1, c2 = ord(s1[i - 1]), ord(s2[j - 1])
                if not i * j:
                    d[i][j] = d[i - 1][j] + c1 if i else d[i][j - 1] + c2 if j else 0
                elif s1[i - 1] == s2[j - 1]: 
                    d[i][j] = d[i - 1][j - 1]
                else: 
                    d[i][j] = min(d[i - 1][j] + c1, d[i][j - 1] + c2, d[i - 1][j - 1] + c1 + c2)
        return d[-1][-1]