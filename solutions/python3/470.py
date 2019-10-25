class Solution:
    def rand10(self):
        return sum(rand7() for _ in range(10)) % 10 + 1