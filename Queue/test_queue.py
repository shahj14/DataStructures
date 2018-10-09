from queue import *
from pytest import fixture

@fixture
def init_queue():
	test_queue = Queue()
	return test_queue

def test_enqueue(init_queue):
	init_queue.enqueue(5)
	assert init_queue.size() == 1
	init_queue.enqueue(7)
	assert init_queue.size() == 2

def test_dequeue(init_queue):
	assert init_queue.dequeue() == None
	init_queue.enqueue(7)
	init_queue.enqueue(9)
	dequeued = init_queue.dequeue()
	assert init_queue.size() == 1
	assert dequeued == 7

def test_peek_queue(init_queue):
	assert init_queue.peek() == None
	init_queue.enqueue(5)
	init_queue.enqueue(7)
	assert init_queue.peek() == 5

def test_size_queue(init_queue):
	assert init_queue.size() == 0
	init_queue.enqueue(5)
	init_queue.enqueue(7)
	assert init_queue.size() == 2

def test_empty_queue(init_queue):
	assert init_queue.empty() == True
	init_queue.enqueue(5)
	assert init_queue.empty() == False