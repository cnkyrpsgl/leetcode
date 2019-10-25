class Solution:
    def shoppingOffers(self, price, special, needs):
        def dfs(cur, needs):
            val = cur + sum(p * needs[i] for i, p in enumerate(price))
            for s in special:
                if all(n >= s[i] for i,n in enumerate(needs)): val = min(val, dfs(cur + s[-1], [n - s[i] for i,n in enumerate(needs)]))
            return val
        return dfs(0, needs)