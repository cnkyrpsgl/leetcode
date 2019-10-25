class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack,res,cur=[],[],[]
        for i in range(len(expression)):
            v=expression[i]
            if v.isalpha():
                cur=[c+v for c in cur or ['']]
            elif v=='{':
                stack.append(res)
                stack.append(cur)
                res,cur=[],[]
            elif v=='}':
                pre=stack.pop()
                preRes=stack.pop()
                cur=[p+c for c in res+cur for p in pre or ['']]
                res=preRes
            elif v==',':
                res+=cur
                cur=[]
        return sorted(set(res+cur))
        