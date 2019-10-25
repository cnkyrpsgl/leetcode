class Solution:
    def findRotateSteps(self, ring, key):
        ind, n, dp, pre = collections.defaultdict(list), len(ring), [0] * len(ring), key[0]
        for i, c in enumerate(ring): ind[c].append(i)
        for i in ind[key[0]]: dp[i] = min(i, n - i) + 1
        for c in key[1:]:
            for i in ind[c]: dp[i] = min(dp[j] + min(i - j, j + n - i) if i >= j else dp[j] + min(j - i, i + n - j) for j in ind[pre]) + 1
            pre = c
        return min(dp[i] for i in ind[key[-1]])