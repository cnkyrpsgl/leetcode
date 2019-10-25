class Solution(object):
    def magicalString(self, n):
        cnt, s, two = 0, "1", True
        for i in range(n - 1):
            if s[i] == "1":
                cnt += 1
                s += "2" if two else "1"
            else: s += "22" if two else "11"
            two = not two
        return cnt if n != 1 else 1