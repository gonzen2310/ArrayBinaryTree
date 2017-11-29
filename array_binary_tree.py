#!/usr/bin/env python3

from binary_tree import BinaryTree
from dynamic_array import DynamicArray


class ArrayBinaryTree(BinaryTree, DynamicArray):

    # noinspection PyPep8Naming,PyPep8Naming,PyMethodMayBeStatic
    def printExpression(self, v):
        pass


def main():
    arr = ArrayBinaryTree()
    test1 = ["-", "*", "+", "-", "2", "*", "5", "+", "7", None, None, "10", "4", None, None, "2", "3"]
    test2 = ["-", "/", "+", "*", "+", "*", "6", "+", "3", "-", "2", "3", "-", None, None, "3", "1", None, None, "9",
             "5", None, None, None, None, "7", "4"]

    arr.printExpression(test1)
    print(test1)
    print(test2)


if __name__ == '__main__':
    main()
