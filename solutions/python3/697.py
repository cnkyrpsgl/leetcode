class Solution:
    def findShortestSubArray(self, nums):
        cnt, seen = collections.Counter(nums), collections.defaultdict(list)
        degree = max(cnt.values())
        for i, v in enumerate(nums): seen[v].append(i)
        return min(seen[v][-1] - seen[v][0] + 1 for v in cnt if cnt[v] == degree)