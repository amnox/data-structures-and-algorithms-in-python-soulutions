# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

def create_list(current_node, next_node, i, arr = []):
    new_node = ListNode(0)
    if i == len(arr)-1:
        current_node.val = arr[i]
        return
    current_node.next = next_node
    current_node.val = arr[i]
    create_list(next_node, new_node, i+1, arr)

def print_list(node):
    if node.next==None:
        print (node.val)
        return
    print(node.val)
    print_list(node.next)

node = ListNode(0)
create_list(node, ListNode(0), 0 , [1,2,3,4,5])
print_list(node)