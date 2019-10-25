class Solution:
    def letterCombinations(self, digits):
        dic, res = { '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}, [""]
        for dig in digits:
            tmp = []
            for y in res: 
                for x in dic[dig]: tmp.append(y + x)
            res = tmp 
        return res if any(res) else []