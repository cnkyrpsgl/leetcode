class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not k:
            return 0
        cnt = collections.Counter()
        i = res = 0
        for j, c in enumerate(s):
            while len(cnt) == k and c not in cnt:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    cnt.pop(s[i])
                i += 1
            cnt[c] += 1
            res = max(res, j - i + 1)
        return res