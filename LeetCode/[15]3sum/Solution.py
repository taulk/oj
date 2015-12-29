class Solution(object):
    def twoSum(self, nums, target):
        i = 0
        j = len(nums) - 1
        res = []
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                res += [[-target, nums[i], nums[j]]]
                i += 1
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                return [nums]
        for i in range(len(nums)-2):
            l = self.twoSum(nums[i+1:], -nums[i])
            res += l
                
        return [list(t) for t in set([tuple(l) for l in res])]
