# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = []

        remain = 0
        while l1 != None or l2 != None:
            value =  (0 if l1 == None else l1.val) + (0 if l2 == None else l2.val) + remain
            if value > 9:
                res.append(value-10)
                remain=1
            else:
                res.append(value)
                remain=0
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if remain == 1:
            res.append(1)
        return res
