from BST import *

def depth(root):
    if root is None:
        return 0
    
    leftCount = height(root.left)
    rightCount = height(root.right)
    
    if leftCount > rightCount:
        return leftCount + 1
    return rightCount + 1	


def isBST(root):
	return isBST_helper(root, -2000, 2000)

def isBST_helper(node, min, max):
	if node is None:
		return True

	return node.data > min and node.data < max and isBST_helper(node.left, min, node.data) and isBST_helper(node.right, node.data, max)		

def isSymmetric(root):
	pass