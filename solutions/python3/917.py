class Solution:
    def reverseOnlyLetters(self, S):
        r = [s for s in S if s.isalpha()]
        return "".join(S[i] if not S[i].isalpha() else r.pop() for i in range(len(S)))