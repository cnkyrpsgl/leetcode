class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        n, pos = str(N), 0
        for i, char in enumerate(n):
            if i>0 and int(n[i])<int(n[i-1]): return int("".join(n[:pos])+str(int(n[pos])-1)+"9"*(len(n)-1-pos)) if int(n[pos])>1 else int("9"*(len(n)-1-pos))
            elif i>0 and n[i] != n[i-1]: pos = i
        return N