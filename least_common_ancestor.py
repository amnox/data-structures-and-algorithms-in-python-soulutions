# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """


def create_tree(arr=[]):
    bauss_node = TreeNode(arr.pop(0))
    next_up = []
    next_up.append(bauss_node)
    while len(arr) >= 1:
        a = next_up.pop(0)
        b = TreeNode(arr.pop(0))
        c = TreeNode(arr.pop(0))
        a.left = b
        a.right = c
        next_up.append(b)
        next_up.append(c)
    return bauss_node

ass = create_tree([3,5,1,6,2,0,8,None,None,7,4])
def printTree(node):
    if node==None:
        return
    printTree(node.left)
    printTree(node.right)

printTree(ass)
def trace_node(target, node, parents=[]):

    if node is not None:
        if target == node.val:
            print(node.val, parents)
            return
        if node.val is not None:
            print(node.val, parents)
            if node.left is not None and node.right is not None:
                parents.append(node.val)
            else:
                print ("fukk: ",node.val)
                parents.pop()
            trace_node(target, node.left, parents)
            trace_node(target, node.right, parents)



trace_node(8,ass)