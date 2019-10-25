class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        bfs = [(0, '')]
        for c in s:
            new = []
            c = int(c)
            for cur, st in bfs:
                if cur * 10 + c <= 255 and (st[-1:] != '0' or cur):
                    new.append((cur * 10 + c, st + str(c)))
                if st:
                    new.append((c, st + '.' + str(c)))
            bfs = new
        return [st for cur, st in bfs if st.count('.') == 3]