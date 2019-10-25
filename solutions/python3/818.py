class Solution:
    def racecar(self, target):
        q, cnt, used = [(0, 1)], 0, {(0, 1)}
        while q:
            new = []
            for pos, speed in q:
                if pos == target:
                    return cnt
                elif pos > 20000 or -20000 > pos:
                    continue
                if (pos + speed, speed * 2) not in used:
                    new.append((pos + speed, speed * 2))
                    used.add((pos + speed, speed * 2))
                if speed > 0 and (pos, -1) not in used:
                    new.append((pos, -1))
                    used.add((pos, -1))
                elif speed < 0 and (pos, 1) not in used:
                    new.append((pos, 1))
                    used.add((pos, 1))
            q = new
            cnt += 1