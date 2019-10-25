class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        used, mod, cnt = set(), 1 % K, 1
        while mod:
            mod = (mod * 10 + 1) % K
            cnt += 1
            if mod in used:
                return -1
            used.add(mod)
        return cnt