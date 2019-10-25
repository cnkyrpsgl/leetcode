class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        cnt, res = {s: [float('inf'), 0] for s in string.ascii_lowercase}, []
        for w in A:
            for k, v in collections.Counter(w).items():
                cnt[k][0] = min(cnt[k][0], v)
                cnt[k][1] += 1
        for k in cnt:
            if cnt[k][1] == len(A):
                res += [k] * cnt[k][0]
        return res