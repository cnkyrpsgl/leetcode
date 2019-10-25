from collections import Counter as cnt


class Solution:
    def maxScoreWords(self, w: List[str], l: List[str], s: List[int]) -> int:
        def dfs(use, i):
            return (
                use
                and i < len(w)
                and max(
                    dfs(use, i + 1),
                    not cnt(w[i]) - use
                    and sum(s[ord(c) - ord("a")] for c in w[i])
                    + dfs(use - cnt(w[i]), i + 1),
                )
            )

        return int(dfs(cnt(l), 0))
