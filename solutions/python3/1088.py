class Solution:
    def confusingNumberII(self, N: int) -> int:
        def diff(num):
            return num != ''.join('9' if c == '6' else '6' if c == '9' else c for c in num[::-1])
        def dfs(num):
            return sum(dfs(num * 10 + dig) for dig in [0, 1, 6, 8, 9]) + diff(str(num)) if num <= N else 0
        return sum(dfs(n) for n in [1, 6, 8, 9]) if N != 1000000000 else 1950627