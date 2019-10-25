class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        memo = {}
        def dfs(l, r, cnt):
            if (l, r, cnt) in memo:
                return memo[(l, r, cnt)]
            if l >= r:
                return True
            elif s[l] != s[r]:
                cnt += 1
                if cnt > 1:
                    memo[(l, r, cnt)] = False
                    return False
                elif (s[l + 1] == s[r] and dfs(l + 1, r, cnt + 1)) or (s[l] == s[r - 1] and dfs(l, r - 1, cnt + 1)):
                    memo[(l, r, cnt)] = True
                    return True
                else:
                    memo[(l, r, cnt)] = False
                    return False
            else:
                memo[(l, r, cnt)] = dfs(l + 1, r - 1, cnt)
                return memo[(l, r, cnt)]
        return dfs(0, len(s) - 1, 0)