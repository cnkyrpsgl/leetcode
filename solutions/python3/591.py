class Solution:
    def isValid(self, S):
        CDATA_BEGIN = '![CDATA['
        CDATA_END = ']]>'

        def collect_tag(i):
            for j in range(i, len(S)):
                if S[j] == '>': break
            else:
                return None
            return S[i+1:j]

        def valid_tag(tag):
            return 1 <= len(tag) <= 9 and all('A' <= c <= 'Z' for c in tag)

        if not S or S[0] != '<': return False
        tag = collect_tag(0)
        if (tag is None or 
                not S.startswith('<{}>'.format(tag)) or 
                not S.endswith('</{}>'.format(tag)) or
                not valid_tag(tag)):
            return False
        S = S[len(tag) + 2: -len(tag) - 3]

        i = 0
        stack = []
        while i < len(S):
            if S[i] == '<':
                tag = collect_tag(i)
                if tag is None: return False
                if tag.startswith(CDATA_BEGIN):
                    while i < len(S) and S[i:i+3] != CDATA_END:
                        i += 1
                    if not S[i:i+3] == CDATA_END:
                        return False
                    i += 2
                elif tag.startswith('/'):
                    tag = tag[1:]
                    if not valid_tag(tag) or not stack or stack.pop() != tag:
                        return False
                else:
                    if not valid_tag(tag):
                        return False
                    stack.append(tag)
            i += 1

        return not stack