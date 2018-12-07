#!/usr/bin/env python
# encoding: utf-8
"""
@author: cbr
"""


class Node(object):
    def __init__(self, data=-1, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class Tree(object):
    def __init__(self):
        self.root = Node()
        self.queue = []

    def add_node(self, ele):
        node = Node(ele)
        if self.root.data == -1:
            self.root = node
            self.queue.append(node)
        else:
            # left tree
            now_node = self.queue[0]
            if now_node.left_child is None:
                now_node.left_child = node
                self.queue.append(node)
            elif now_node.right_child is None:
                now_node.right_child = node
                self.queue.append(node)
                # remove completed node(both left and right)
                self.queue.pop(0)

    """implements different iterations by recursive way"""
    def front_recursive(self, root):
        if root is None:
            return
        print(root.data),
        self.front_recursive(root.left_child)
        self.front_recursive(root.right_child)

        # ...

    """implements different iterations by stack way"""
    @staticmethod
    def front_stack(root):
        if root is None:
            return
        q = []
        node = root

        while node or q:
            while node:
                print(node.data),
                q.append(node)
                node = node.left_child
            # left tree is empty
            node = q.pop().right_child

    @staticmethod
    def mid_stack(root):
        if root is None:
            return
        q = []
        node = root

        while node or q:
            while node:
                q.append(node)
                node = node.left_child
            node = q.pop()  # pop last
            print(node.data),
            node = node.right_child

    @staticmethod
    def later_stack(root):
        if root is None:
            return
        q1 = []
        q2 = []
        node = root
        q1.append(node)

        while q1:
            node = q1.pop()
            if node.left_child:
                q1.append(node.left_child)
            if node.right_child:
                q1.append(node.right_child)
            q2.append(node)

        while q2:
            print(q2.pop().data),

    @staticmethod
    def level_iter(root):
        if root is None:
            return
        q = []
        node = root
        q.append(node)

        while q:
            node = q.pop(0)
            print(node.data),
            if node.left_child:
                q.append(node.left_child)
            if node.right_child:
                q.append(node.right_child)


if __name__ == '__main__':
    t_s = range(10)
    tree = Tree()
    for i in t_s:
        tree.add_node(i)
    print("*" * 10)
    print("the seq %s" % t_s)
    print("*" * 10)
    print("front recursive")
    tree.front_recursive(tree.root)
    print("\nfront stack")
    tree.front_stack(tree.root)
    print("\nmid stack")
    tree.mid_stack(tree.root)
    print("\nlater stack")
    tree.later_stack(tree.root)
    print("\nlevel iter")
    tree.level_iter(tree.root)