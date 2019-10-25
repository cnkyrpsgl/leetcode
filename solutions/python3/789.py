class Solution:
    def escapeGhosts(self, ghosts, target):
        d = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            if abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) <= d: return False
        return True