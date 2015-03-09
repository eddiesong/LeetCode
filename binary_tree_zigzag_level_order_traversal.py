# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def preorder(self, root, level, ans):
    	if root:
    		if len(ans) < level+1:
	    		ans.append([])
	    	if level % 2 == 0:
	    	    ans[level].append(root.val)
	    	else:
	    	    ans[level].insert(0, root.val)
	    	self.preorder(root.left, level+1, ans)
	    	self.preorder(root.right, level+1, ans)
    def zigzagLevelOrder(self, root):
        ans = []
        if root == None:
        	return ans
        self.preorder(root, 0, ans)
        return ans
        