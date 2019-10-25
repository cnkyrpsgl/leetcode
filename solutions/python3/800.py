class Solution:
    def similarRGB(self, color):
        """
        :type color: str
        :rtype: str
        """
        import math
        num1, num2, num3 = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)
        letters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        min1, min2, min3, res = math.inf, math.inf, math.inf, ["#","","",""]
        for letter in letters:
            min1, min2, min3 = min(min1,(num1-int(letter*2,16))**2), min(min2,(num2-int(letter*2,16))**2), min(min3,(num3-int(letter*2,16))**2) 
            if min1 == (num1-int(letter*2,16))**2: res[1] = letter*2 
            if min2 == (num2-int(letter*2,16))**2: res[2] = letter*2 
            if min3 == (num3-int(letter*2,16))**2: res[3] = letter*2
        return "".join(res)