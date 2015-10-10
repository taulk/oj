###
# Manacher's Algorithm
# ref:http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
###
class Solution(object):
    def extend(self, s):
        es = ['#']*(2*len(s)+1)
        es[1::2] = s
        return "".join(es)
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str = self.extend(s)
        
        i, mx, id = 0, 0, 0

        p = [0]*len(str)

        while i < len(str):
            if mx > i:
                p[i] = min(p[2*id-i], mx-i)
            else:
                p[i] = 1
            while i-p[i] >= 0 and i+p[i] < len(str) and str[i-p[i]] == str[i+p[i]]:
                p[i] += 1
            if mx < p[i]+i:
                mx = p[i] + i
                id = i
            i += 1
        c, ml = 0, 0
        for i in range(len(str)):
            if p[i] > ml:
                ml = p[i]
                c = i
        return str[c-ml+2:c+ml][::2]
