class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        re, im = 0, 0
        re_a, im_a = list(map(int,a[:-1].split("+")))
        re_b, im_b = list(map(int,b[:-1].split("+")))
        re += re_a * re_b - im_a * im_b
        im += re_a * im_b + re_b *im_a
        return str(re)+"+"+str(im)+"i"