class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        m = len(wall)
        sm = sum(wall[0])
        cnt = collections.defaultdict(int)
        for i in range(m):
            x = 0
            for num in wall[i]:
                x += num
                if x != sm:
                    cnt[x] += 1
        mx = 0
        for i in range(m):
            x = 0
            for num in wall[i]:
                x += num
                mx = max(mx, cnt[x])
        return m - mx