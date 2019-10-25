class Solution:
    def romanToInt(self, s):
        table = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        sm, pre = 0, 'I'
        for c in s[::-1]: 
            if table[c] < table[pre]:
                sm, pre = sm - table[c], c  
            else:
                sm, pre = sm + table[c], c
        return sm