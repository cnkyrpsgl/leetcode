class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        count=0
        prev_count=0
        for letter in s:
            if count>0:
                prev_count=count
            if letter==" ":
                count=0
                continue
            count+=1
        if count>0:
            return count
        else:
            return prev_count