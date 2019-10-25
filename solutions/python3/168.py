class Solution:
    def convertToTitle(self, n: int) -> str:
        char = str()
        while n > 0:
            if n % 26 == 0:
                char += "Z"
                n = n // 26 - 1
            else:
                char += chr(n % 26 + ord("@"))
                n = n // 26
        return char[::-1]
