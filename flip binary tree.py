class BinaryTree:
    def __init__(self, value=0, left=None, right=None, parent=None):
        self._left = left
        self._right = right
        self._parent = parent
        self._value = value

    def value(self):
        return self._value

    def left(self):
        return self._left

    def right(self):
        return self._right

    def parent(self):
        return self._parent

    def sibling(self):
         parent = self.parent()
         if parent==None :
             return None
         elif parent.right() == self:
             return parent.left()
         elif parent.left() == self:
             return parent.right()


def populateTree(node,left,right):
    print("shit")


root = BinaryTree(1, BinaryTree(2), BinaryTree(3))


def printTree(node):
    if node==None:
        return
    print(node.value())
    printTree(node.left())
    printTree(node.right())

printTree(root)