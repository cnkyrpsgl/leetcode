class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        def root(a):
            return a if parent[a] == a else root(parent[a])
        parent = [i for i in range(N)]
        time = -1
        for t, a, b in sorted(logs):
            A, B = root(a), root(b)
            parent[A] = parent[a] = parent[b] = B
            if A != B:
                time = t
        return time if all(root(a) == root(b) for a, b in zip(parent, parent[1:])) else -1