class Solution(object):
    def maxK(self, nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.maxK(nums2, nums1, k)

        if len(nums1) == 0:
            return nums2[k-1]
        if k == 1:
            if nums1[0] > nums2[0]:
                return nums2[0]
            else:
                return nums1[0]

        if len(nums1) > k/2:
           index1 = k/2
        else:
            index1 = len(nums1)
        index2 = k - index1

        if nums1[index1-1] > nums2[index2-1]:
            return self.maxK(nums1, nums2[index2:], k-index2)
        elif nums1[index1-1] < nums2[index2-1]:
            return self.maxK(nums1[index1:], nums2, k-index1)
        else:
            return nums1[index1-1]
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        count = len(nums1) + len(nums2)
        if count % 2 == 1:
            return self.maxK(nums1, nums2, count/2+1)
        else:
            return (self.maxK(nums1, nums2, count/2) + self.maxK(nums1, nums2, count/2+1))/2.0
