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
				yield lst

def insertion_sort(lst):
	indexing_length = range(1, len(lst))
	for i in indexing_length:
		value_to_sort = lst[i]

		while lst[i-1] > value_to_sort and i > 0:
			lst[i], lst[i-1] = lst[i-1], lst[i]
			i -= 1
			yield lst
