class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        s = strs[0]
        j = 0
        for j in range(len(s)):
            for i in range(len(strs)):
                if j >= len(strs[i]):
                    return s[0:j]
                if strs[i][j] != s[j]:
                    return s[0:j]
        return s
