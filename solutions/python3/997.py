class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        j, cnt = collections.Counter(b for a, b in trust).most_common(1)[0] if trust else (N, 0)
        return j if j not in {a for a, b in trust} and cnt == N - 1 else -1