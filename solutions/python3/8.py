class Solution:
    def myAtoi(self, str):
        r = [int(c) for c in re.findall(r"^[-+]?\u005Cd+", str.lstrip())]
        return (r and 2 ** 31 - 1 < r[0] and 2 ** 31 - 1) or (r and r[0] < -2 ** 31 and -2 ** 31) or (r and r[0]) or 0