from random import randrange
from sorting_algorithms import *
from graphics import update, Text, Point
from text_sorting.Runner import Runner
class SortingAlgorithm:

	sorts = [insertion_sort, bubble_sort]
	sortsText = ["Insertion Sort","Bubble Sort"]
	sorts_text = {sorts[0] : sortsText[0], sorts[1] : sortsText[1]}
	
	def __init__(self, window, amountTowers):
		self.win = window
		self.runner = Runner()
		self.lst = []
		self.generateList(amountTowers)
		self.currentSort = self.sorts[0]
		self.currentSortText = Text(Point(150, 775), f"Current Sort: {self.sorts_text[self.currentSort]}")
		self.currentSortText.setSize(15)
		self.currentSortText.draw(self.win)

	def generateList(self, number):
		#for i in range(number):
			#self.lst.append(randrange(100, self.win.getHeight()-200))
		lst = self.runner.makeLst(30)
		for i, number in enumerate(lst):
			lst[i] = number*20
		self.lst = lst

	def clear(self):
		self.lst.clear()

	def getList(self):
		return self.lst

	def switchSort(self, key):
		for sort in self.sorts:
			if self.sortsText.lower()[0] == key:
				pass

	def sort(self, ascending=True):
		for lst in self.currentSort(self.lst):
			self.win.drawList(lst, ascending)
			update(60)

	def alternateSort(self):
		currentSortIndex = self.sorts.index(self.currentSort)
		try:
			self.currentSort = self.sorts[currentSortIndex+1]
		except IndexError:
			self.currentSort = self.sorts[0]
		self.currentSortText.setText(f"Current Sort: {self.sorts_text[self.currentSort]}")