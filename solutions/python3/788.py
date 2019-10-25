class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        for i in range(1, N + 1):
            i = str(i)
            tmp = []
            check = True
            for char in i:
                if char in ("3", "4", "7"):
                    check = False
                    break
                if char in ("0", "1", "8"):
                    tmp.append(char)
                if char == "2":
                    tmp.append("5")
                if char == "5":
                    tmp.append("2")
                if char == "6":
                    tmp.append("9")
                if char == "9":
                    tmp.append("6")
            if check and i != "".join(tmp): res += 1
        return res