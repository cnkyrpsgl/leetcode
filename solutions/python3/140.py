class Solution:
    def wordBreak(self, s, wordDict):
        def breakable():
            rightmosts = [0]
            for i in range(1, len(s) + 1):
                for last_index in rightmosts:
                    if s[last_index:i] in words:
                        rightmosts.append(i)
                        if i == len(s): 
                            return True
                        break
            return False
        q, res, words = [("", 0)], [], set(wordDict)
        if breakable():
            for j in range(1, len(s) + 1):
                new = q[:]
                for seq, i in q:
                    if s[i:j] in words:
                        if j == len(s):
                            res.append(seq and seq + " " + s[i:j] or s[i:j])
                        else:
                            new.append((seq and seq + " " + s[i:j] or s[i:j], j))
                q = new
        return res