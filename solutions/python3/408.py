class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = num = 0
        for c in abbr:
            if c.isdigit():
                if num == 0 and c == '0':
                    return False
                num = num * 10 + int(c)
            else:
                if num:
                    #print(i, num)
                    i += num 
                    num = 0
                if i >= len(word) or word[i] != c:
                    #print(i, c)
                    return False
                i += 1
        return i == len(word) if num == 0 else i + num == len(word)