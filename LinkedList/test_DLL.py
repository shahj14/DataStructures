from DLL import DLinkedList
from pytest import fixture, raises

@fixture
def init_list():
	test_list = DLinkedList()
	return test_list

@fixture
def full_list():
	test_list = DLinkedList()
	test_list.addFirst(3)
	test_list.addFirst(8)
	test_list.addFirst(5)
	return test_list

def test_add_first(init_list):
	init_list.addFirst(4)
	init_list.addFirst(5)
	assert init_list.length() == 2
	assert init_list.getHead() == 5
	assert init_list.getTail() == 4

def test_add_last(init_list):
	init_list.addLast(5)
	init_list.addLast(7)
	init_list.addLast(6)
	assert init_list.length() == 3
	assert init_list.getHead() == 5
	assert init_list.getTail() == 6

def test_delete_first(full_list):
	assert full_list.deleteFirst() == 5
	assert full_list.deleteFirst() == 8
	assert full_list.deleteFirst() == 3
	with raises(Exception):
		full_list.deleteFirst() == None

def test_delete_last(full_list):
	assert full_list.deleteLast() == 3
	assert full_list.deleteLast() == 8
	assert full_list.deleteLast() == 5
	with raises(Exception):
		full_list.deleteLast() == None

def test_empty(init_list, full_list):
	assert init_list.empty() == True
	assert full_list.empty() == False

def test_length(init_list, full_list):
	assert init_list.length() == 0
	assert full_list.length() == 3