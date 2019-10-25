class Solution:
    def minKBitFlips(self, a: List[int], k: int) -> int:
        q = collections.deque()
        res = 0
        for i in range(len(a)):
            if len(q) % 2 != 0 and a[i] == 1 or len(q) % 2 == a[i] == 0:
                res += 1
                q.append(i+k-1)
            if q and q[0] == i: q.popleft()
            if q and q[-1] >= len(a): return -1
        return res