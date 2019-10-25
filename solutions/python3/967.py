class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        q = {i for i in range(10)}
        for _ in range(N - 1):
            new = set()
            for num in q:
                last = num % 10
                if num and 0 <= last + K <= 9:
                    new.add(num * 10 + last + K)
                if num and 0 <= last - K <= 9:
                    new.add(num * 10 + last - K)
            q = new
        return list(q)