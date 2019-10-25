class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        return True if s=="" or [i.lower() for i in s if i in string.digits or i in string.ascii_letters]==[i.lower() for i in s if i in string.digits or i in string.ascii_letters][::-1] else False