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
        if head.next==None:
            return None
        def find_len(node, i = 1):
            if node.next is None:
                return i
            return find_len(node.next, i+1)

        def pop_ops(current_pos, popy, node, prev_node):

            if node.next is None:
                prev_node.next=None
                return
            if current_pos == popy:
                if prev_node is None:
                    node = None
                    return
                else:
                    print('else',current_pos, popy)
                    prev_node.next = node.next
                    return
            pop_ops(current_pos+1, popy, node.next, node)



        pop_at = find_len(head) - n + 1
        if(pop_at==1):
            head = head.next
            return head
        pop_ops(1, pop_at, head, None)
        return head


def create_list(current_node, next_node, i, arr=[]):
    new_node = ListNode(0)
    if i == len(arr)-1:
        current_node.val = arr[i]
        return
    current_node.next = next_node
    current_node.val = arr[i]
    create_list(next_node, new_node, i+1, arr)


def print_list(node):
    if node.next is None:
        print(node.val)
        return
    print(node.val)
    print_list(node.next)


node = ListNode(0)
create_list(node, ListNode(0), 0, [1, 2])
Solution().removeNthFromEnd(node, 2)
print_list(node)
