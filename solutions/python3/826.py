class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted([a, b] for a, b in zip(difficulty, profit))
        res = i = maxp = 0
        for ability in sorted(worker):
            while i < len(jobs) and ability >= jobs[i][0]:
                maxp = max(jobs[i][1], maxp)
                i += 1
            res += maxp
        return res      