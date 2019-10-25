class Solution:
    def getHint(self, secret, guess):
        s, g, a, b = collections.defaultdict(int), collections.defaultdict(int), 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]: a += 1; continue
            if s[guess[i]] > 0: b, s[guess[i]] = b + 1, s[guess[i]] - 1
            else: g[guess[i]] += 1
            if g[secret[i]] > 0: b, g[secret[i]] = b + 1, g[secret[i]] - 1
            else: s[secret[i]] += 1
        return "%dA%dB" % (a, b)