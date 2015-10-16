class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -self.reverse(-x)
        s = str(x)
        i = int(s[::-1])
        if i > 2147483647:
            return 0
        return i
