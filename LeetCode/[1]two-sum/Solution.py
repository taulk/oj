class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        sortednums = sorted(nums)
        length = len(nums)
        left = 0
        right = length - 1
        res = []
        while left < right:
            sum = sortednums[left] + sortednums[right]
            if sum == target:
                for i in range(length):
                    if nums[i] == sortednums[left]:
                        res.append(i+1)
                    elif nums[i] == sortednums[right]:
                        res.append(i+1)
                    if len(res) == 2:
                        return res
            if sum < target:
                left += 1
            else:
                right -= 1
