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

Approach 2:
BFS
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):

            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)

            mid = current_node == p or current_node == q

            if mid + left + right >= 2:
                self.ans = current_node

            return mid or left or right
        recurse_tree(root)
        return self.ans
