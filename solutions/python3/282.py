class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # s, val, cur, coeff
        q = {("", 0, 0, 1)}
        for i, c in enumerate(num):
            new = set()
            for s, val, cur, coeff in q:
                if i:
                    new.add((s + "+" + c, val + int(c), int(c), 1))
                    new.add((s + "-" + c, val - int(c), int(c), -1))
                    new.add((s + "*" + c, val + cur * coeff * (int(c) - 1), int(c), cur * coeff))
                if s and s[-1] == "0" and cur == 0: continue
                pre = cur
                cur = cur * 10 + int(c)
                new.add((s + c, val + coeff * (cur - pre), cur, coeff))
            q = new
        return [s for s, val, cur, coeff in q if val == target]