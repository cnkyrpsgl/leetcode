class Solution:
    def openLock(self, deadends, target):
        moved, q, cnt, move = set(deadends), ["0000"], 0, {str(i): [str((i + 1) % 10), str((i - 1) % 10)] for i in range(10)}
        if "0000" in moved:
            return -1
        while q:
            new = []
            cnt += 1
            for s in q:
                for i, c in enumerate(s):
                    for cur in (s[:i] + move[c][0] + s[i + 1:], s[:i] + move[c][1] + s[i + 1:]):
                        if cur not in moved:
                            if cur == target:
                                return cnt
                            new.append(cur)
                            moved.add(cur)
            q = new
        return -1