class Solution:
    def movesToStamp(self, stamp, target):
        def okay(s):
            ret = False
            for c1, c2 in zip(s, stamp):
                if c1 == "*": continue
                elif c1 != c2: return False
                else: ret = True
            return ret
        t, move, mx, arr = "*" * len(target), 0, 10 * len(target), []
        while move < mx:
            pre = move
            for i in range(len(target) - len(stamp) + 1):
                if okay(target[i:i + len(stamp)]):
                    move += 1
                    arr = [i] + arr
                    target = target[:i] + "*" * len(stamp) + target[i + len(stamp):]
            if target == t: return arr
            if move == pre: break
        return []