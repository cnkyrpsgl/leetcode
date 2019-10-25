class Solution:
    def isNumber(self, s):
        s = s.strip()
        pointSeen = eSeen = numberSeen = False
        numberAfterE = True
        for i, c in enumerate(s):
            if "0" <= c <= "9":
                numberSeen = numberAfterE = True
            elif c == ".":
                if eSeen or pointSeen:
                    return False
                pointSeen = True
            elif c == "e":
                if eSeen or not numberSeen:
                    return False
                numberAfterE = False
                eSeen = True
            elif c in "-+":
                if i and s[i - 1] != "e":
                    return False
            else:
                return False
        return numberSeen and numberAfterE