from BST import BST
from pytest import fixture

@fixture
def empty_tree():
	test_tree = BST()
	return test_tree

@fixture
def full_tree():
	test_tree = BST()
	test_tree.insert(5)
	test_tree.insert(8)
	test_tree.insert(3)
	test_tree.insert(4)
	return test_tree

def test_insert(empty_tree):
	empty_tree.insert(4)
	empty_tree.insert(9)
	empty_tree.insert(8)
	assert empty_tree.empty() == False
	assert empty_tree.getRoot().data == 4
	assert empty_tree.getRoot().left == None
	assert empty_tree.getRoot().right.left.data == 8

def test_exists(empty_tree, full_tree):
	assert empty_tree.exists(4) == False
	assert full_tree.exists(4) == True
	assert full_tree.exists(9) == False

def test_get_min(empty_tree, full_tree):
	assert empty_tree.getMin() == None
	assert full_tree.getMin() == 3

def test_get_max(empty_tree, full_tree):
	assert empty_tree.getMax() == None
	assert full_tree.getMax() == 8

def test_empty(empty_tree, full_tree):
	assert empty_tree.empty() == True
	assert full_tree.empty() == False