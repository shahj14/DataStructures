from BST import *

def depth(root):
    if root is None:
        return 0
    
    leftCount = depth(root.left)
    rightCount = depth(root.right)
    
    if leftCount > rightCount:
        return leftCount + 1
    return rightCount + 1	


def isBST(root):
	inf = 1000
	return isBST_helper(root, -inf, inf)

def isBST_helper(node, min, max):
	if node is None:
		return True

	if node.data < min or node.data > max:
		return False	

	return isBST_helper(node.left, min, node.data) and isBST_helper(node.right, node.data, max)		

#check if both sides of the tree are the mirrors of each other
def isSymmetric(root):
	if root is None:
		return True	
	return symHelper(root.left, root.right)

def symHelper(leftTree, rightTree):
	if leftTree is None or rightTree is None:
		return leftTree is None and rightTree is None

	return leftTree.data == rightTree.data and symHelper(leftTree.left, rightTree.right) and symHelper(leftTree.right, rightTree.left)	