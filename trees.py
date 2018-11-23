class Tree:

    class Position:
        """An abstraction representing the location of a single element."""
        def element(self):
            raise NotImplementedError('Must Be Implemented By subclass')

        def __eq__(self, other):
            """To check if other position represents same position"""
            raise NotImplementedError('Must Be Implemented By subclass')

        def __ne__(self, other):
            """Return true if other does not represent same location"""
            return not (self == other)

    def root(self):
        """Return Position representing Tree's Root"""
        raise NotImplementedError('Must Be Implemented By subclass')

    def parent(self, p):
        """Return position representing p's parent"""
        raise NotImplementedError('Must Be Implemented By subclass')

    def num_children(self, p):
        """Return number of children that position p has"""
        raise NotImplementedError('Must Be Implemented By subclass')

    def children(self, p):
        """Generate an iteration of positions representing p's children"""
        raise NotImplementedError('Must Be Implemented By subclass')

    def __len__(self):
        """Return total number of elements in the tree"""
        raise NotImplementedError('Must Be Implemented By subclass')

    def is_root(self, p):
        """Return true if p is root of the tree"""
        return self.root() == p

    def is_leaf(self, p):
        """Returns true if p does not have any children"""
        return self.num_children(p) == 0

    def is_empty(self):
        """Returns true if Tree is empty"""
        return len(self) == 0

    def depth(self, p):
        """Returns number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

