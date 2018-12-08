'''
Approach 1: Recursive Approach
Intuition

The approach is pretty intuitive. Traverse the tree in a depth first manner. The moment you encounter either of the nodes p or q, return some boolean flag. The flag helps to determine if we found the required nodes in any of the paths. The least common ancestor would then be the node for which both the subtree recursions return a True flag. It can also be the node which itself is one of p or q and for which one of the subtree recursions returns a True flag.

Let us look at the formal algorithm based on this idea.

Algorithm

Start traversing the tree from the root node.
If the current node itself is one of p or q, we would mark a variable mid as True and continue the search for the other node in the left and right branches.
If either of the left or the right branch returns True, this means one of the two nodes was found below.
If at any point in the traversal, any two of the three flags left, right or mid become True, this means we have found the lowest common ancestor for the nodes p and q.
Let us look at a sample tree and we search for the lowest common ancestor of two nodes 9 and 11 in the tree.

Following is the sequence of nodes that are followed in the recursion:

1 --> 2 --> 4 --> 8
BACKTRACK 8 --> 4
4 --> 9 (ONE NODE FOUND, return True)
BACKTRACK 9 --> 4 --> 2
2 --> 5 --> 10
BACKTRACK 10 --> 5
5 --> 11 (ANOTHER NODE FOUND, return True)
BACKTRACK 11 --> 5 --> 2

2 is the node where we have left = True and right = True and hence it is the lowest common ancestor.
'''
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
    print(node.val)
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
                if node.left.val is None and node.right.val is None:
                    print("fukk",node.val)
                else:
                    parents.append(node.val)

            trace_node(target, node.left, parents)
            trace_node(target, node.right, parents)



trace_node(8,ass)