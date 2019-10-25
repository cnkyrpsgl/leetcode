class Solution:
    def shiftingLetters(self, S, shifts):
        sm, res = sum(shift % 26 for shift in shifts) % 26, ""
        for i, s in enumerate(shifts):
            move, sm = ord(S[i]) + sm % 26, sm - s
            res += chr(move > 122 and move - 26 or move)
        return res