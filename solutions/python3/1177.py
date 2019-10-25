class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnts = [{}]
        for i, c in enumerate(s):
            cnts.append(dict(cnts[-1]))
            cnts[-1][c] = cnts[-1].get(c, 0) + 1
        res = []
        for i, j, k in queries:
            res.append(sum((v - cnts[i].get(k, 0)) % 2 for k, v in cnts[j + 1].items()) - k * 2 <= 1)
        return res
        
        