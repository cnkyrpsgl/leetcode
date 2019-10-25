class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        curr, count, i = chars[0], 1, 1
        while i<len(chars):
            if chars[i]!=curr:
                curr=chars[i]
                if count>1: chars[:i]+= (i for i in "".join(str(count))); i+=len([i for i in "".join(str(count))])
                i, count =i+1, 1
            else:
                if i==len(chars)-1: chars.pop(i); chars+=[i for i in "".join(str(count+1))]; break
                chars.pop(i); count+=1
        return len(chars)      