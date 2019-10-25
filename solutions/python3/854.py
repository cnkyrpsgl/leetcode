class Solution:
    def kSimilarity(self, A, B):
        b, n, k, stack = [c for c in B], len(A), float("inf"), [(0, 0, [c for c in A])]
        while stack:
            i, cnt, s = stack.pop()
            while i < n and s[i] == b[i]:
                i += 1
            if i == n:
                if cnt < k:
                    k = cnt
            else:
                for j in range(i + 1, n):
                    if s[j] == b[i] and s[j] != b[j]:
                        ls = s[:]
                        ls[i], ls[j] = ls[j], ls[i]
                        stack.append((i + 1, cnt + 1, ls))
        return k