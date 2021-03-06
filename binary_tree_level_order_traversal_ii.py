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
	    	ans[level].append(root.val)
	    	self.preorder(root.left, level+1, ans)
	    	self.preorder(root.right, level+1, ans)
    def levelOrderBottom(self, root):
        ans = []
        if root == None:
        	return ans
        self.preorder(root, 0, ans)
        ans.reverse()
        return ans