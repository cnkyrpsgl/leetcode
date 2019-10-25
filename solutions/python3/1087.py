class Solution:
    def permute(self, S: str) -> List[str]:
        bfs = [""]
        mult = False
        chars = []
        for s in S:
            if s == ',': 
                continue
            elif s == '{':
                mult = True
            elif s == '}':
                bfs = [st + c for st in bfs for c in chars]
                chars = []
                mult = False
            elif mult:
                chars.append(s)
            else:
                bfs = [st + s for st in bfs]
        return sorted(bfs)
                