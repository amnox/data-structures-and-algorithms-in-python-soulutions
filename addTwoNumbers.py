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
        def purify_number(list,mul,len):
            if list.next==None or mul==len:
                return int(int(list.val)*int(10**mul))
            return int(int(list.val)*int(10**mul)) + purify_number(list.next,mul+1,len)
        def impurify_number(list,linknow,linknext):
            dig = list.pop()
            linknow.val = dig
            if len(list)<1:
                return
            linknow.next = linknext
            #print(list, linknow.val)
            impurify_number(list,linknext,ListNode(0))

        def print_arr(linklist, val=[]):

            if (linklist.next == None):
                val.append(linklist.val)
                return val
            val.append(linklist.val)
            return print_arr(linklist.next)
        l1_len = len(print_arr(l1))
        l2_len = len(print_arr(l2))
        sum = [int(x) for x in str(int(purify_number(l1,0,l1_len) + purify_number(l2,0,l2_len)))]
        final = ListNode(0)
        impurify_number(sum,final,ListNode(0))
        return(final)


def impurify_number(list,linknow,linknext):


    dig = list.pop(0)
    linknow.val = dig
    if len(list)<1:
        return
    linknow.next = linknext
    #print(list, linknow.val)
    impurify_number(list,linknext,ListNode(0))


def print_arr(linklist, val=[]):

    if (linklist.next == None):
        val.append(linklist.val)
        return val
    else:
        val.append(linklist.val)
        return print_arr(linklist.next)

eed = ListNode(1)
eed.next = eed2 = ListNode(3)
eed2.next = eed3 = ListNode(7)

ood = ListNode(6)
ood.next = ood2 = ListNode(0)
ood2.next = ood3 = ListNode(2)
arr1 = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
arr2 = [5,6,4]
link1 = ListNode(0)
link2 = ListNode(0)
impurify_number(arr1,link1,ListNode(0))
impurify_number(arr2,link2,ListNode(0))
#print(print_arr(link1))
print(print_arr(Solution().addTwoNumbers(link1,link2)))

