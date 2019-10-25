class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        cnt = collections.Counter()
        for b in B:
            for k, v in collections.Counter(b).items():
                if cnt[k] < v:
                    cnt[k] = v
        res = []
        for a in A:
            if not cnt - collections.Counter(a):
                res.append(a)
        return res