class Solution:
    def numRabbits(self, answers):
        dic, res = {}, 0
        for ans in answers:
            (dic[ans], res) = (1, res + ans + 1) if ans not in dic or dic[ans] > ans else (dic[ans] + 1, res)
        return res