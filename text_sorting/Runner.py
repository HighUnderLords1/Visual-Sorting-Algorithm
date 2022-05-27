from .sorting_algorithms import *
from random import randint, choice
from time import time
import os
import sys
import json
class Runner:
	def __init__(self):
		self.lengths = [100, 500, 10000, 100000, 1000000, 2000000]

	def makeLst(self, length):
		lst = []

		with open("C:\\Users\\Joseph Stambaugh\\Dropbox\\My PC (UnknownDevice)\\Desktop\\sorting_algorithms\\lists\\lists.json", "r") as f:
			data = json.loads(f.read())

		allLists = data.get(str(length))
		if allLists:
			lst = choice(allLists)
		else:
			return

		#for i in range(length):
			#number = randint(1, length)
			#lst.append(number)
		return lst

	def calc_bubble_sort(self):
		times = []

		for length in self.lengths:
			lst = self.makeLst(length)
			print(length)
			startTime = time()
			lst = bubble_sort(lst)
			endTime = time()
			timeTook = endTime - startTime
			print(timeTook)
			times.append(timeTook)
		return times

	def calc_insertion_sort(self):
		times = []

		for length in self.lengths:
			lst = self.makeLst(length)
			print(length)
			startTime = time()
			lst = insertion_sort(lst)
			endTime = time()
			timeTook = endTime - startTime
			print(timeTook)
			times.append(timeTook)

		return times

	def calc_quick_sort(self):
		times = []

		for length in self.lengths:
			lst = self.makeLst(length)
			print(length)
			startTime = time()
			lst = quick_sort(lst, 0, len(lst)-1)
			endTime = time()
			timeTook = endTime - startTime
			print(timeTook)
			times.append(timeTook)

		return times

	def calc_merge_sort(self):
		times = []

		for length in self.lengths:
			lst = self.makeLst(length)
			print(length)
			startTime = time()
			lst = merge_sort(lst)
			endTime = time()
			timeTook = endTime - startTime
			print(timeTook)
			times.append(timeTook)

		return times

	def saveSortTime(self, name, times):
		with open("text_sorting/times.json", "r") as f:
			data = json.loads(f.read())
			data[name] = times
		data = json.dumps(data)
		with open("text_sorting/times.json", "w") as f:
			f.write(data)

	def calc_all(self):
		print("Quick")
		quick_times = self.calc_quick_sort()
		self.saveSortTime("Quick Sort", quick_times)
		#print("Bubble")
		#bubble_times = self.calc_bubble_sort()
		#self.saveSortTime("Bubble Sort", bubble_times)
		#print("Insertion")
		#insertion_times = self.calc_insertion_sort()
		#self.saveSortTime("Insertion Sort", insertion_times)
		print("Merge")
		merge_times = self.calc_merge_sort()
		self.saveSortTime("Merge Sort", merge_times)

	def getTimesText(self):
		string = ""
		with open("text_sorting/times.json", "r") as f:
			data = json.loads(f.read())
		merge_times = data["Merge Sort"]
		quick_times = data["Quick Sort"]
		lengths = ["30", "100", "500", "10,000", "1,000,000", "2,000,000"]
		string += "Lengths|"
		maxLength = len(lengths[len(lengths)-1])
		for i, length in enumerate(lengths):
			numberLength = len(length)
			if i != len(lengths)-1:
				string += length.zfill(maxLength - numberLength)+" | "
			else:
				string += length+"\n"
		#print(string)
		mergeStr = "Merge  | "
		for i, time in enumerate(merge_times):
			number = round(float(time), 3)
			numberLength = len(str(number))
			#print(lengths[i], len(lengths[i]))
			#print(number, numberLength)
			if i != len(merge_times)-1:
				mergeStr += str(number).zfill(maxLength-numberLength+1) + " | "
			else:
				mergeStr += str(number).zfill(maxLength-numberLength) + "\n"
		string += mergeStr
		quickStr = "Quick  | "
		for i, time in enumerate(quick_times):
			number = round(float(time), 3)
			numberLength = len(str(number))
			#print(lengths[i], len(lengths[i]))
			#print(number, numberLength)
			if i != len(merge_times)-1:
				quickStr += str(number).zfill(maxLength-numberLength+1) + " | "
			else:
				quickStr += str(number).zfill(maxLength-numberLength)
		string+=quickStr
		return string

		
	