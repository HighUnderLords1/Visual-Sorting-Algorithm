from graphics import *
from SortingAlgorithm import SortingAlgorithm
from Window import Window
from Button import Button
from random import choice
from text_sorting.Runner import Runner
import json

def changeColors(win, colors):
	c1 = choice(colors)
	c2 = choice(colors)
	while c1 == c2:
		c2 = choice(colors)
	win.setColors(c1, c2)

def clear():
	import os
	os.system("cls")

def printTimes():
	runner = Runner()
	timesText = runner.getTimesText()
	clear()
	print(timesText)

def main():
	colors = ["yellow", "orange", "red", "blue", "purple", "pink", "green"]
	amount = 30
	win = Window(amount)
	sort_algo = SortingAlgorithm(win, amount)
	lastLst = sort_algo.getList()
	lst = sort_algo.getList()
	win.drawList(lst)
	ascending = True
	sorting = False
	mustRefresh = False
	running = True
	refreshText = Text(Point(150, 750), "Refresh")
	refreshText.setFill('red')
	refreshText.setSize(15)
	ascendingText = Text(Point(400, 775), f"Ascending = {ascending}")
	ascendingText.setSize(15)
	ascendingText.draw(win)
	keysText = Text(Point(650, 750), "Space: Sort, A: Ascending\nD: Descending, R: Refresh\nS, Switch Algo, Q: Exit")
	keysText.setSize(15)
	keysText.draw(win)
	seeTimes = Button(win, Point(150, 700), 100, 50, "See Times")
	seeTimes.activate()
	while running:
		key = win.checkKey()
		mouse = win.checkMouse()
		#if key:
			#print(key)

		if mouse:
			if seeTimes.clicked(mouse):
				printTimes()

		lst = sort_algo.getList()
		if lst != lastLst:
			win.drawList(lst, ascending)
			lastLst = lst
		
		if key == 'q' or key == "Escape":
			win.close()
			running = False
		elif key == "space" and not mustRefresh:
			sorting = True
			sort_algo.sort(ascending)
			sorting = False
		elif key == "r" and not sorting:
			print("Please Wait")
			sort_algo.clear()
			sort_algo.generateList(amount)
			win.drawList(sort_algo.getList(), ascending)
			mustRefresh=False
			clear()
		elif key == "a":
			ascending = True
			mustRefresh = True
		elif key == "d":
			ascending = False
			mustRefresh = True
		elif key == "s":
			sort_algo.alternateSort()
		elif key == "c":
			changeColors(win, colors)
			mustRefresh = True

		ascendingText.setText(f"Ascending = {ascending}")
		
		if mustRefresh:
			try:
				refreshText.draw(win)
			except:
				pass
		else:
			refreshText.undraw()

	win.close()


def makeLsts():
	"WARNING: THIS USES A LOT OF MEMORY"
	from lists.generateLsts import generateLsts
	for length in [30, 100, 500, 10000, 100000, 1000000, 2000000]:
		for i in range(10):
			print(length, i+1)
			generateLsts(length, length)

def calcSpeeds():
	from text_sorting.Runner import Runner
	runner = Runner()
	runner.calc_all()

def test():
	pass

if __name__ == "__main__":
	try:
		main()
	except GraphicsError:
		clear()
		exit("Goodbye")