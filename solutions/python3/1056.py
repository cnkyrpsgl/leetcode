class Solution:
    def confusingNumber(self, N: int) -> bool:
        ret = ''.join("01####9#86"[int(n)] for n in str(N)[::-1])
        return '#' not in ret and ret != str(N)