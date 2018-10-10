from SLL import LinkedList
from pytest import fixture

@fixture
def init_list():
	test_list = LinkedList()
	return test_list

@fixture
def full_list():
	test_list = LinkedList()
	test_list.addFirst(5)
	test_list.addFirst(8)
	test_list.addFirst(10)
	return test_list

def test_add_first(init_list):
	init_list.addFirst(5)
	init_list.addFirst(8)
	assert init_list.size() == 2

def test_delete_first(full_list):
	assert full_list.deleteFirst() == 10
	assert full_list.deleteFirst() == 8
	assert full_list.deleteFirst() == 5
	assert full_list.deleteFirst() == None

def test_add_last(init_list):
	init_list.addLast(5)
	init_list.addLast(8)
	assert init_list.size() == 2
	assert init_list.deleteFirst() == 5

def test_delete_last(full_list):
	assert full_list.deleteLast() == 5
	assert full_list.deleteLast() == 8
	assert full_list.deleteLast() == 10
	assert full_list.deleteLast() == None

def test_empty(init_list, full_list):
	assert init_list.empty() == True
	assert full_list.empty() == False

def test_size(init_list, full_list):
	assert init_list.size() == 0
	assert full_list.size() == 3	
