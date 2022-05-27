from random import randint
import time
def swap(n1, n2):
	return n2, n1

def bubble_sort(lst):
	n = len(lst)
	for i in range(1, n):
		for j in range(0, n-1):
			if lst[j] > lst[j + 1]:
				lst[j], lst[j+1] = swap(lst[j], lst[j+1])
	return lst

def insertion_sort(lst):
	indexing_length = range(1, len(lst))
	for i in indexing_length:
		value_to_sort = lst[i]

		while lst[i-1] > value_to_sort and i > 0:
			lst[i], lst[i-1] = lst[i-1], lst[i]
			i -= 1

	return lst

def quick_sort(lst, left, right):
	if left >= right:
		return

	pivot = lst[(left + right)//2]
	index = partition(lst, left, right, pivot)
	quick_sort(lst, left, index-1)
	quick_sort(lst, index, right)
	

def partition(lst, left, right, pivot):
	while left <= right:
		while lst[left] < pivot:
			left += 1

		while lst[right] > pivot:
			right -= 1

		if left <= right:
			lst[left], lst[right] = lst[right], lst[left]
			left+=1
			right-=1

	return left

def merge_sort(lst):
	if len(lst) == 1:
		return lst

	middle = len(lst)//2
	left = lst[0 : middle]
	right = lst[middle: len(lst)]

	return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
	result = []
	indexLeft = 0
	indexRight = 0

	while indexLeft < len(left) and indexRight < len(right):
		if left[indexLeft] < right[indexRight]:
			result.append(left[indexLeft])
			indexLeft+=1
		else:
			result.append(right[indexRight])
			indexRight+=1

	return result+left[indexLeft:len(left)]+right[indexRight:len(right)]