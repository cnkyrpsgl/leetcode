class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        m1 = b - 1 - a
        m2 = c - b - 1
        m1 + m2
        if a + 2 == b or b + 2 == c:
            return [1, m1 + m2]
        n1 = int(b - 1 > a)
        n2 = int(b + 1 < c)
        return [n1 + n2, m1 + m2]       
                