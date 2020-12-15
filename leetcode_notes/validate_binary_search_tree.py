# coding=utf-8
"""
leetcode:98题：验证二叉搜索树
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
        A valid BST is defined as follows:
        The left subtree of a node contains only nodes with keys less than the node's key.
        The right subtree of a node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees must also be binary search trees.
"""

 # 方法一：利用二叉树的特性，采用中树遍历
def isValidBST(self, root):
    inorder = self.inorder(root)
    return inorder == list(sorted(set(inorder)))

def inorder(self, root):
    if root is None:
        return []
    return self.inorder(root.left) + [root.val] + self.inorder(root.right)

# 方法二
def isValidBST2(self, root):
    self.prev = None
    return self.helper(root)

def helper(self, root):
    if root is None:
        return True
    if not self.helper(root.left):
        return False
    if self.prev and self.prev.val >= root.val:
        return False
    self.prev = root 
    return self.helper(root.right)
