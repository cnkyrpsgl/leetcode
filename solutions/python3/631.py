class Excel(object):

    def __init__(self, H, W):
        self.M = [[{'v': 0, 'sum': None} for i in range(H)] for j in range(ord(W) - 64)]

    def set(self, r, c, v):
        self.M[r - 1][ord(c) - 65] = {'v': v, 'sum': None}

    def get(self, r, c):
        cell = self.M[r - 1][ord(c) - 65]
        if not cell['sum']: return cell['v']
        return sum(self.get(*pos) * cell['sum'][pos] for pos in cell['sum'])

    def sum(self, r, c, strs):
        self.M[r - 1][ord(c) - 65]['sum'] = self.parse(strs)
        return self.get(r, c)

    def parse(self, strs):
        c = collections.Counter()
        for s in strs:
            s, e = s.split(':')[0], s.split(':')[1] if ':' in s else s
            for i in range(int(s[1:]), int(e[1:]) + 1):
                for j in range(ord(s[0]) - 64, ord(e[0]) - 64 + 1):
                    c[(i, chr(j + 64))] += 1
        return c