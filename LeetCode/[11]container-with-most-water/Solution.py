class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height)-1
        res = 0
        while i<j:
            res = max(res, min(height[i], height[j]) * (j-i))
            if height[i] > height[j]:
                j = j - 1
            else:
                i = i + 1
        return res
