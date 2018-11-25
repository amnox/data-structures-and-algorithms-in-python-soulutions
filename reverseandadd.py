# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
import math
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def purify_number(list,mul):
            if list.next==None:
                return list.val*math.pow(10,mul)
            return list.val*math.pow(10,mul) + purify_number(list.next,mul+1)
        def impurify_number(list,linknow,linknext):


            dig = list.pop()
            linknow.val = dig
            if len(list)<1:
                return
            linknow.next = linknext
            print(list, linknow.val)
            impurify_number(list,linknext,ListNode(0))

        sum = [int(x) for x in str(int(purify_number(l1,0) + purify_number(l2,0)))]
        final = ListNode(0)
        impurify_number(sum,final,ListNode(0))
        return(final)

eed = ListNode(1)
eed.next = eed2 = ListNode(3)
eed2.next = eed3 = ListNode(7)

ood = ListNode(6)
ood.next = ood2 = ListNode(0)
ood2.next = ood3 = ListNode(2)

Solution().addTwoNumbers(eed,ood)

