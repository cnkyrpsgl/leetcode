class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.dp = collections.defaultdict(list)
        for i, v in enumerate(arr):
            self.dp[v].append(i)
        self.occur = sorted([(len(v), k) for k, v in self.dp.items()], reverse = True)
        
    def query(self, left: int, right: int, threshold: int) -> int:
        for o, v in self.occur:
            if o < threshold: break
            l = self.dp[v]
            low = bisect.bisect_left(l, left)
            high = bisect.bisect_right(l, right)
            if high - low >= threshold:
                return v
        return -1