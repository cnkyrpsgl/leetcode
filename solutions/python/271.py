class Codec:

    def encode(self, strs):
        return "".join(str(len(s)) + ":" + s for s in strs)

    def decode(self, s):
        strs = []
        while s:
            i = s.find(":")
            length = int(s[:i])
            s = s[i+1:]
            strs.append(s[:length])
            s = s[length:]
        return strs