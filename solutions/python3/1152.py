class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dp = collections.defaultdict(list)
        count = collections.Counter()
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        for u in dp:
            count += collections.Counter(set(seq for seq in itertools.combinations(dp[u], 3)))
        target = max(count.values())
        return min(list(k) for k in count if count[k] == target)