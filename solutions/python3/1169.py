class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        last = collections.defaultdict(list)
        ret = set()
        for n, t, a, c in sorted([t.split(',') for t in transactions], key = lambda x: int(x[1])):
            if int(a) > 1000:
                ret.add(','.join([n, t, a, c]))
            if n in last:
                for tt, aa, cc in last[n][::-1]:
                    if int(t) - int(tt) > 60:
                        break
                    if cc != c:
                        ret.add(','.join([n, tt, aa, cc]))
                        ret.add(','.join([n, t, a, c]))
            last[n].append([t, a, c])
        return list(ret)
        