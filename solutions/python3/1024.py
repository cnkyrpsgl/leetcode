class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key = lambda x: (-x[0], x[1]))
        x = cnt = mx = 0
        while clips and clips[-1][0] <= x < T:
            while clips and clips[-1][0] <= x:
                mx = max(mx, clips.pop()[1])
            if mx > x:
                x = mx
                cnt += 1
        return cnt if x >= T else -1