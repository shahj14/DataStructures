from BST import *
from tree_practice import *
from pytest import fixture

@fixture
def empty_tree():
	test_tree = None
	return test_tree

@fixture
def three_tree():
	test_tree = Node(5, Node(6), Node(7, Node(8)))	
	return test_tree

@fixture
def four_tree():
	test_tree = Node(5, Node(6, Node(8, Node(9))), Node(7, Node(8)))	
	return test_tree

@fixture
def full_binary_tree():
	test_tree = BST()
	test_tree.insert(5)
	test_tree.insert(8)
	test_tree.insert(9)
	test_tree.insert(2)
	test_tree.insert(4)
	return test_tree

@fixture
def not_binary_tree():
	test_tree = Node(5, Node(4, right=Node(6)))
	return test_tree

@fixture
def sym_tree():
	test_tree = Node(5, Node(6, left=Node(7)), Node(6, right=Node(7)))
	return test_tree

def test_tree_level(empty_tree, three_tree, four_tree):
	assert depth(empty_tree) == 0 #test empty tree
	assert depth(three_tree) == 3	
	assert depth(four_tree) == 4

def test_is_bst(full_binary_tree, not_binary_tree):
	assert isBST(full_binary_tree.getRoot()) == True
	assert isBST(not_binary_tree) == False

def test_is_sym(four_tree, three_tree, full_binary_tree, sym_tree):	
	assert isSymmetric(four_tree) == False
	assert isSymmetric(three_tree) == False
	assert isSymmetric(full_binary_tree.getRoot()) == False
	assert isSymmetric(sym_tree) == True


