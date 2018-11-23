class Tree:

    class Position:

        def element(self):
            raise NotImplementedError('Must Be Implemented By subclass')

        def __eq__(self, other):
            raise NotImplementedError('Must Be Implemented By subclass')

        def __ne__(self, other):
            return not (self == other)

    def root(self):
        raise NotImplementedError('Must Be Implemented By subclass')

    def parent(self, p):
        raise NotImplementedError('Must Be Implemented By subclass')

    def num_children(self, p):
        raise NotImplementedError('Must Be Implemented By subclass')

    def children(self, p):
        raise NotImplementedError('Must Be Implemented By subclass')

    def len(self):
        raise NotImplementedError('Must Be Implemented By subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

