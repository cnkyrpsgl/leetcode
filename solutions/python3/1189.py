class Solution:
    def maxNumberOfBalloons(self, t: str) -> int:
          return min(t.count(c) // 'balloon'.count(c) for c in 'balon')