class Solution:
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        l, r, score = 0, len(tokens) - 1, 0
        while l <= r:
            if P >= tokens[l]:
                P -= tokens[l]
                score += 1
                l += 1
            elif score and l != r:
                P += tokens[r]
                score -= 1
                r -= 1
            else:
                break
        return score