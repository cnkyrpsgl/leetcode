class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        s = ''.join(bin(int(num))[2:].zfill(8) for num in ip.split('.'))
        res = []
        while n:
            for i in range(31 - s.rindex('1'), -1, -1):
                if 2 ** i <= n:
                    res.append('.'.join(str(int(s[i:i + 8], 2)) for i in range(0, 32, 8)) + '/' + str(32 - i))
                    n -= 2 ** i
                    s = bin(int(s, 2) + 2 ** i)[2:].zfill(32)
                    break
        return res
        