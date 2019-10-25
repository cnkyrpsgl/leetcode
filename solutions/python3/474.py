class Solution:
    def findMaxForm(self, strs, m, n):
        res = [0]
        memo = set()
        def dfs(st, zeros, ones, cnt):
            if (zeros, ones, cnt) not in memo:
                if cnt > res[0]:
                    res[0] = cnt
                if zeros or ones:
                    for s in st:
                        if st[s] and cntr[s]["0"] <= zeros and cntr[s]["1"] <= ones:
                            st[s] -= 1
                            dfs(st, zeros - cntr[s]["0"], ones - cntr[s]["1"], cnt + 1)
                            st[s] += 1
                memo.add((zeros, ones, cnt))
                
        cntr = {s:collections.Counter(s) for s in strs}
        dfs(collections.Counter(strs), m, n, 0)
        return res[0]