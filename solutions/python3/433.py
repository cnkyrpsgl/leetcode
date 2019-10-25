class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bfs = [start]
        genes = set(bank)
        cnt = 0
        while bfs:
            arr = []
            for g in bfs:
                if g == end:
                    return cnt
                for i, c in enumerate(g):
                    for new in 'AGTC':
                        if new != c:
                            s = g[:i] + new + g[i + 1:]
                            if s in genes:
                                arr.append(s)
                                genes.discard(s)
            bfs = arr
            cnt += 1
        return -1