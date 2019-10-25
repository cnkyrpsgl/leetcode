from functools import lru_cache

class Solution:
    def numMusicPlaylists(self, N, L, K):
        @lru_cache(None)
        def dp(i, j): return +(j == 0) if not i else (dp(i-1, j-1) * (N-j+1) + dp(i-1, j) * max(j-K, 0)) % (10**9+7)
        return dp(L, N)