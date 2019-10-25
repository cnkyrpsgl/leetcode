class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def uf(c):
            return uf(parent[ord(c) - ord('a')]) if parent[ord(c) - ord('a')] != c else ord(c) - ord('a')
        parent = [c for c in string.ascii_lowercase]
        for eq in equations:
            if eq[1] == '=':
                parent[uf(eq[0])] = parent[uf(eq[-1])]
        for eq in equations:
            if eq[1] == '!' and parent[uf(eq[0])] == parent[uf(eq[-1])]:
                return False
        return True