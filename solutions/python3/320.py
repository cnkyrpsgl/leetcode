class Solution:
    def generateAbbreviations(self, word):
        l, res = len(word), []
        def dfs(s, i):
            if i == l:
                res.append(s)
            else:
                dfs(s + word[i], i + 1)
                if not s or s[-1] > "9":
                    for j in range(i + 1, l + 1):
                        dfs(s + str(j - i), j)
        dfs("", 0)
        return res