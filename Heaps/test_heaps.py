from heaps import MinHeap, MaxHeap
from pytest import fixture

@fixture
def init_min_heap():
	test_heap = MinHeap()
	return test_heap

@fixture
def init_max_heap():
	test_heap = MaxHeap()
	return test_heap	

@fixture
def full_min_heap():
	test_heap = MinHeap()
	test_heap.add(4)
	test_heap.add(6)
	test_heap.add(3)
	test_heap.add(7)
	test_heap.add(5)
	return test_heap

@fixture
def full_max_heap():
	test_heap = MaxHeap()
	test_heap.add(4)
	test_heap.add(6)
	test_heap.add(3)
	test_heap.add(7)
	test_heap.add(5)
	return test_heap

def test_min_add(init_min_heap):
	init_min_heap.add(4)
	init_min_heap.add(8)
	assert init_min_heap.size() == 2
	assert init_min_heap.getHeap() == [4,8]

def test_min_poll(init_min_heap, full_min_heap):
	assert init_min_heap.poll() == None
	assert full_min_heap.poll() == 3
	assert full_min_heap.poll() == 4
	assert full_min_heap.size() == 3

def test_max_add(init_max_heap):
	init_max_heap.add(4)
	init_max_heap.add(8)
	assert init_max_heap.size() == 2
	assert init_max_heap.getHeap() == [8,4]

def test_max_poll(init_max_heap, full_max_heap):
	assert init_max_heap.poll() == None
	assert full_max_heap.poll() == 7
	assert full_max_heap.poll() == 6
	assert full_max_heap.size() == 3	








