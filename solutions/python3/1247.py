class Solution:
    def minimumSwap(self, s1: str, s2: str, xy: int = 0, yx: int = 0) -> int:
        for a, b in zip(s1, s2):
            xy += a == "x" and b == "y"
            yx += a == "y" and b == "x"
        return (xy + yx) // 2 + (xy % 2) * 2 if xy % 2 == yx % 2 else -1
