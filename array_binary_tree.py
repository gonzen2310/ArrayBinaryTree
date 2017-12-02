#!/usr/bin/env python3

from binary_tree import BinaryTree
from dynamic_array import DynamicArray


class ArrayBinaryTree(BinaryTree, DynamicArray):
    def __init__(self):
        DynamicArray.__init__(self)
        BinaryTree.__init__(self)

    # TREE METHODS

    # noinspection PyProtectedMember
    class Position:
        def __init__(self, index, element):
            self._index = index
            self._element = element

        def __eq__(self, other):
            if type(other) is ArrayBinaryTree.Position:
                return self._index == other._index
            else:
                return False

        def element(self):
            return self._element

    def parent(self, p):
        # noinspection PyProtectedMember
        i = p._index
        if i == 0:
            return None
        else:
            parent_idx = (i - 1) // 2
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
        if left_idx >= len(self):
            return None
        if self[left_idx] is None:
            return None
        else:
            return self[left_idx]

    # noinspection PyProtectedMember
    def right(self, p):
        right_idx = p._index * 2 + 2
        if right_idx >= self._n:
            return None
        elif self[right_idx] is None:
            return None
        else:
            return self[right_idx]

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def printExpression(self, v):
        if self.left(v) is not None and self.left(v).element() is not None:
            print("(", end="")
            self.printExpression(self.left(v))
        print(v.element(), end="")
        if self.right(v) is not None and self.right(v).element() is not None:
            self.printExpression(self.right(v))
            print(")", end="")


def main():

    test = ArrayBinaryTree()
    a = ArrayBinaryTree.Position(0, '-')
    b = ArrayBinaryTree.Position(1, '/')
    c = ArrayBinaryTree.Position(2, '+')
    d = ArrayBinaryTree.Position(3, '*')
    e = ArrayBinaryTree.Position(4, '+')
    f = ArrayBinaryTree.Position(5, '*')
    g = ArrayBinaryTree.Position(6, '6')
    h = ArrayBinaryTree.Position(7, '+')
    i = ArrayBinaryTree.Position(8, '3')
    j = ArrayBinaryTree.Position(9, '-')
    k = ArrayBinaryTree.Position(10, '2')
    l = ArrayBinaryTree.Position(11, '3')
    m = ArrayBinaryTree.Position(12, '-')
    n = ArrayBinaryTree.Position(13, None)
    o = ArrayBinaryTree.Position(14, None)
    p = ArrayBinaryTree.Position(15, '3')
    q = ArrayBinaryTree.Position(16, '1')
    r = ArrayBinaryTree.Position(17, None)
    s = ArrayBinaryTree.Position(18, None)
    t = ArrayBinaryTree.Position(19, '9')
    u = ArrayBinaryTree.Position(20, '5')
    v = ArrayBinaryTree.Position(21, None)
    w = ArrayBinaryTree.Position(22, None)
    x = ArrayBinaryTree.Position(23, None)
    y = ArrayBinaryTree.Position(24, None)
    z = ArrayBinaryTree.Position(25, '7')
    zz = ArrayBinaryTree.Position(26, '4')

    nodes = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, zz]
    for x in nodes:
        test.append(x)
    print("Test 1:")
    print("length: ", end="")
    print(len(test))
    print("Number of children: ")
    print(test.num_children(a))
    print(test.num_children(v))
    print(test.num_children(h))
    print("Parent Test: ")
    print(test.parent(b).element())
    print("Left Test: ")
    print(test.left(d))
    print("Right Test: ")
    print(test.right(a).element())
    test.printExpression(test.root())
    print("\n")

    test2 = ArrayBinaryTree()
    aa = ArrayBinaryTree.Position(0, '-')
    bb = ArrayBinaryTree.Position(1, '*')
    cc = ArrayBinaryTree.Position(2, '+')
    dd = ArrayBinaryTree.Position(3, '-')
    ee = ArrayBinaryTree.Position(4, '2')
    ff = ArrayBinaryTree.Position(5, '*')
    gg = ArrayBinaryTree.Position(6, '5')
    hh = ArrayBinaryTree.Position(7, '+')
    ii = ArrayBinaryTree.Position(8, '7')
    jj = ArrayBinaryTree.Position(9, None)
    kk = ArrayBinaryTree.Position(10, None)
    ll = ArrayBinaryTree.Position(11, '10')
    mm = ArrayBinaryTree.Position(12, '4')
    nn = ArrayBinaryTree.Position(13, None)
    oo = ArrayBinaryTree.Position(14, None)
    pp = ArrayBinaryTree.Position(15, '2')
    qq = ArrayBinaryTree.Position(16, '3')

    nodes = [aa, bb, cc, dd, ee, ff, gg, hh, ii, jj, kk, ll, mm, nn, oo, pp, qq]
    for y in nodes:
        test2.append(y)
    print("Test 2:")
    print("length: ", end="")
    print(len(test2))
    print("Left Test: ")
    print(test2.left(aa).element())
    print("Right Test: ")
    print(test2.right(aa).element())

    test2.printExpression(test2.root())


if __name__ == '__main__':
    main()
