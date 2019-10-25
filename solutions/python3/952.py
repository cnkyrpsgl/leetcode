class Solution:
    def largestComponentSize(self, A):
        def find(i):
            return i if i == parent[i] else find(parent[i])
        
        def prime_factors(n):  
            res = set()
            while n % 2 == 0: 
                res.add(2)
                n //= 2
            for i in range(3, int(n**0.5) + 1, 2): 
                while n % i== 0: 
                    res.add(i) 
                    n //= i 
            if n > 2: 
                res.add(n)
            return res
        parent, dic = list(range(len(A))), {} 
        for i, n in enumerate(A):
            for p in prime_factors(n):
                if p in dic:
                    parent[find(i)] = find(dic[p])
                dic[p] = i
        for i, x in enumerate(parent):
            parent[i] = find(x)
        return max(collections.Counter(parent).values())