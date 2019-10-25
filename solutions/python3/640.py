class Solution:
    def solveEquation(self, equation):
        def calc(eq):
            smX = smNum = 0
            add, num = True, ""
            for c in eq + "+":
                if c.isdigit():
                    num += c
                elif c == "x":
                    smX += int(num) if add and num else -int(num) if num else 1 if add else -1
                    num = ""
                else:
                    smNum += int(num) if add and num else -int(num) if num else 0
                    num, add = "", c == "+"
            return smX, smNum
        eq = equation.split("=")
        lX, lNum, rX, rNum = calc(eq[0]) + calc(eq[1])
        if lX == rX: 
            return "No solution" if lNum != rNum else "Infinite solutions"
        return "x=" + str((lNum - rNum) // (rX - lX))