class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.findall(r"\u005Cw+", paragraph)
        dic = {}
        mx = [0, 0]
        for char in paragraph:
            char = char.lower()
            if char not in banned:
                if char not in dic: dic[char] = 1
                else: dic[char] += 1
                mx[0] = max(mx[0], dic[char])
                if mx[0] == dic[char]: mx[1] = char
        return mx[1]
        