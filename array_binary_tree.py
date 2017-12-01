#!/usr/bin/env python3

from binary_tree import BinaryTree
from dynamic_array import DynamicArray


class ArrayBinaryTree(BinaryTree, DynamicArray):
    def __init__(self):
        DynamicArray.__init__(self)

    # TREE METHODS

    class Position:
        def __init__(self, index, element):
            self._index = index
            self._element = element

        def __eq__(self, other):
            # noinspection PyProtectedMember
            return self._index == other._index

        def element(self):
            return self._element

    def parent(self, p):
        # noinspection PyProtectedMember
        current_idx = p._index
        if current_idx == 0:
            return None
        else:
            parent_idx = (current_idx - 1) // 2
            return self[parent_idx]

    def __len__(self):
        return self._n

    def root(self):
        if self.is_empty():
            return None
        else:
            return self[0]

    def num_children(self, p):
        if self.left(p) is not None and self.right(p) is not None:
            return 2
        elif self.left(p) is not None or self.right(p) is not None:
            return 1
        else:
            return 0
    # BINARY TREE METHODS

    def left(self, p):
        # noinspection PyProtectedMember
        left_idx = p._index * 2 + 1
        if left_idx > len(self):
            return None
        elif self[left_idx] is None:
            return None
        else:
            return self[left_idx]

    # noinspection PyProtectedMember
    def right(self, p):
        right_idx = p._index * 2 + 2
        if right_idx > self._n:
            return None
        elif self[right_idx] is None:
            return None
        else:
            return self[right_idx]

    # noinspection PyPep8Naming
    def printExpression(self):
        root_tree = self.root()
        if root:
            self.printExpression()
            print(root._element)




def main():
    tree_array = ArrayBinaryTree()
    a = ArrayBinaryTree.Position(0, '-')
    b = ArrayBinaryTree.Position(1, '*')
    c = ArrayBinaryTree.Position(2, '+')
    d = ArrayBinaryTree.Position(3, '-')
    e = ArrayBinaryTree.Position(4, '2')
    f = ArrayBinaryTree.Position(5, '*')
    g = ArrayBinaryTree.Position(6, '5')
    h = ArrayBinaryTree.Position(7, '+')
    i = ArrayBinaryTree.Position(8, '7')
    j = ArrayBinaryTree.Position(9, None)
    k = ArrayBinaryTree.Position(10, None)
    l = ArrayBinaryTree.Position(11, '10')
    m = ArrayBinaryTree.Position(12, '4')
    n = ArrayBinaryTree.Position(13, None)
    o = ArrayBinaryTree.Position(14, None)
    p = ArrayBinaryTree.Position(15, '2')
    q = ArrayBinaryTree.Position(16, '3')

    nodes = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q]
    for x in nodes:
        tree_array.append(x)

    tree_array.printExpression(a)


if __name__ == '__main__':
    main()
