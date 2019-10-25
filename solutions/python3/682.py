class Solution:
    def calPoints(self, ops: List[str]) -> int:
        arr = []
        for op in ops:
            #print(arr)
            if op.isdigit() or op[0] == '-':
                arr.append(int(op))
            elif op == 'C' and arr:
                arr.pop()
            elif op == 'D' and arr:
                arr.append(arr[-1] * 2)
            elif len(arr) >= 2:
                arr.append(arr[-1] + arr[-2])
        #print(arr)
        return sum(arr)