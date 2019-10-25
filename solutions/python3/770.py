class Solution(object):
    def basicCalculatorIV(self, s, evalvars, evalints):
        s.strip()
        d = dict(zip(evalvars, evalints))
        s = s.replace(' ', '')
        ts = re.findall('\u005Cd+|[-()+*]|[^-()+*]+', s)
        
        def add(p, q):
            i, j = 0, 0
            r = []
            while i < len(p) and j < len(q):
                v, c = p[i]
                v2, c2 = q[j]
                if v == v2:
                    if c + c2 != 0:
                        r.append((v, c + c2))
                    i += 1
                    j += 1
                elif len(v) > len(v2) or len(v) == len(v2) and v < v2:
                    r.append(p[i])
                    i += 1
                else:
                    r.append(q[j])
                    j += 1
                            
            r += p[i:]
            r += q[j:]
            return r

        def neg(p):
            r = []
            for v, c in p:
                r.append((v, -c))
            return r

        def sub(p, q):
            return add(p, neg(q))

        def mult(p, q):
            r = []
            for v, c in p:
                for v2, c2 in q:
                    r = add(r, [(sorted(v + v2), c * c2)])
            return r
            
        def prec(c):
            return 0 if c in [')'] else 1 if c in ['+', '-'] else 2
            
        i = 0 
        def expr(p):
            nonlocal i, ts
            if ts[i] == '(':
                i += 1
                v = expr(0)
                i += 1
            elif ts[i] == '-':
                i += 1
                v = neg(expr(3))
            elif re.match('\u005Cd+', ts[i]):
                if ts[i] != '0':
                    v = [([], int(ts[i]))]
                else:
                    v = []
            else:
                if ts[i] in d:
                    if d[ts[i]] != 0:
                        v = [([], d[ts[i]])]
                    else:
                        v  = []
                else:
                    v = [([ts[i]], 1)]
            while i < len(ts) - 2 and prec(ts[i+1]) > p:
                op = ts[i+1]
                i += 2
                v2 = expr(prec(op))
                if op == '+': v = add(v, v2)
                if op == '-': v = sub(v, v2)
                if op == '*': v = mult(v, v2)
                
            return v

        def tostrings(p):
            r = []
            for v, c in p:
                if v == []:
                    r.append(str(c))
                else:
                    r.append(str(c) + '*' + '*'.join(v))
            return r
        
        return tostrings(expr(0))