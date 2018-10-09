from sorts import *
import pytest


inputs =  	[
	([4,3,1,2], [1,2,3,4]),
	([], []),
	([23,10,12,4,56,20], [4,10,12,20,23,56])
]

@pytest.mark.parametrize(("arr", "sorted_arr"), inputs)
def test_insertion_sort(arr, sorted_arr):
	assert insertion_sort(arr) == sorted_arr


@pytest.mark.parametrize(("arr", "sorted_arr"), inputs)
def test_quick_sort(arr, sorted_arr):
	quick_sort(arr, 0, len(arr)-1)
	assert arr == sorted_arr


@pytest.mark.parametrize(("arr", "sorted_arr"), inputs)
def test_merge_sort(arr, sorted_arr):
	merge_sort(arr, 0, len(arr)-1)
	assert arr == sorted_arr