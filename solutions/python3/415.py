class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return "".join(str(sum([(ord(num1[i])-ord("0"))*(10**(len(num1)-1-i)) for i in range(len(num1))]+[(ord(num2[i])-ord("0"))*(10**(len(num2)-1-i)) for i in range(len(num2))])))