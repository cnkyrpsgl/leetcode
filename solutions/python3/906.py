class Solution:
    def superpalindromesInRange(self, L, R):
        L, R = int(L), int(R)
        left = int(math.floor(math.sqrt(L)))
        right = int(math.ceil(math.sqrt(R)))
        n1, n2 = len(str(left)), len(str(right))
        n1 = n1//2 if n1%2==0 else n1//2+1
        n2 = n2//2 if n2%2==0 else n2//2+1
        start = int('1' + '0'*(n1 - 1))
        end = int('9' * n2) + 1
        ans = 0 
        for i in range(start, end):
            x = str(i)
            num1 = int(x + x[::-1])
            num2 = int(x + x[:-1][::-1])
            for num in [num1, num2]:
                cand = num * num
                if L <= cand <= R and str(cand) == str(cand)[::-1]:
                    ans += 1
        return ans