from search import *
import pytest

@pytest.mark.parametrize(("test_arr", "search", "ans"), 
	[
		([1,4,7,8], 5, False),
		([3, 8, 10], 8, True),
		([5,3,9,2], 0, False),
		([10,12,4,7,8], 7, True)
	])
def test_binary_search(test_arr, search, ans):
	assert binary_search(test_arr, search) == ans


@pytest.mark.parametrize(("test_arr", "search", "ans"), 
	[
		([1,4,7,8], 5, 4),
		([3, 8, 10], 12, 10),
		([5,3,9,2], 0, 2),
		([10,12,4,7,8], 7, 7)
	])
def test_binary_search_closest(test_arr, search, ans):
	assert binary_search_closest(test_arr, search) == ans
