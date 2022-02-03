# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        s = []
        if root == None:
            return False
        targetSum -= root.val
        if root.left != None:
            s.append((root.left, targetSum))
        if root.right != None:
            s.append((root.right, targetSum))
        if root.right == None and root.left == None and targetSum == 0:
            return True
        while s:
            node, val = s.pop()
            if node.left != None:
                s.append((node.left, val - node.val))
            if node.right != None:
                s.append((node.right,val - node.val))
            if node.right == None and node.left == None:
                if val - node.val == 0:
                    return True
        return False