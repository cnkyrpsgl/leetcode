class Solution:
    def multiply(self, num1, num2):
        dic, l1, l2 = {str(i): i for i in range(10)}, len(num1) - 1, len(num2) - 1
        return str(sum([dic[n1] * (10**(l1-i)) for i, n1 in enumerate(num1)]) * sum([dic[n2] * (10**(l2-j)) for j, n2 in enumerate(num2)]))