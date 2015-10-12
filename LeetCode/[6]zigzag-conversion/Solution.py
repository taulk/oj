class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) < 2 or numRows == 1:
            return s
        sub_str = []
        for i in range(1, numRows-1):
            s1 = s[i:len(s):2*numRows-2]
            s2 = s[2*(numRows-1)-i:len(s):2*numRows-2]
            sub = [0] * (len(s1)+len(s2))
            sub[::2] = s1
            sub[1::2] = s2
            sub_str += sub
        return s[::2*numRows-2]+"".join(str(x) for x in sub_str)+s[numRows-1:len(s):2*numRows-2]
