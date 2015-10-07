class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        left = -1
        right = 0
        max = 0
        if len(s) < 2:
            return len(s)
        while right < len(s)-1:
            d[s[right]] = right
            right += 1
            if d.has_key(s[right]) and d[s[right]] > left:
                left = d[s[right]]
            if right - left > max:
                max = right - left
        return max
