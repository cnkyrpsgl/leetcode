class Solution:
    def countLetters(self, S: str) -> int:
        cnt = collections.Counter()
        i = res = 0
        for j, c in enumerate(S):
            cnt[c] += 1
            while len(cnt) > 1:
                cnt[S[i]] -= 1
                if not cnt[S[i]]:
                    cnt.pop(S[i])
                i += 1
            res += j - i + 1
        return res
                
            