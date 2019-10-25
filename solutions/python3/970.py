class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        res = set()
        i = j = 0
        while x ** i <= bound:
            while x ** i + y ** j <= bound:
                if x ** i + y ** j not in res:
                    res.add(x ** i + y ** j)
                j += 1
                if y == 1: 
                    break
            j = 0
            i += 1
            if x == 1:
                break
        return list(res)
