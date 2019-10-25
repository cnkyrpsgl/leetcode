class Solution:
    def toGoatLatin(self, S):
        s, vowels = S.split(), {"a", "e", "i", "o", "u"} 
        return " ".join([(s[i][0].lower() in vowels and s[i] or s[i][1:] + s[i][0]) + "m" + "a" * (i + 2) for i in range(len(s))])