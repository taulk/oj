class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        m = 0
        i = len(s) - 1
        sum = 0
        while i >= 0:
            if d[s[i]] >= m:
                sum = sum + d[s[i]]
            else:
                sum = sum - d[s[i]]
            m = d[s[i]]
            i = i - 1
        return sum
