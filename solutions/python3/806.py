class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        left=0
        lines=1
        for char in S:
            if left+widths[ord(char)-ord("a")]<=100:
                left+=widths[ord(char)-ord("a")]
            else:
                lines+=1
                left=widths[ord(char)-ord("a")]
        return [lines, left]