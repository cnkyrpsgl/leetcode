class Solution:
    def toHex(self, num):
        if not num: return "0"
        mp, ans = "0123456789abcdef", ""
        for i in range(8):
            n = num & 15       
            c = mp[n]          
            ans = c + ans
            num = num >> 4
        return ans.lstrip('0')