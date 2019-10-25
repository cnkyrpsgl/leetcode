class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        cnt = collections.Counter(S[:K - 1])
        res = 0
        for i in range(K - 1, len(S)):
            cnt[S[i]] += 1
            if len(cnt) == K:
                res += 1
            cnt[S[i - K + 1]] -= 1
            if not cnt[S[i - K + 1]]:
                cnt.pop(S[i - K + 1])
        return res