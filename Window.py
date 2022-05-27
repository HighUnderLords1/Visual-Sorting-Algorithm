from graphics import *
from random import choice
class Window(GraphWin):
	def __init__(self, amountTowers):
		super().__init__("Sorting Algorithm", 800, 800, autoflush = False)
		self.setCoords(0,0,self.getWidth(),self.getHeight())

		self.colors = ['red', 'blue']
		self.colorDict = {}
		self.amountTowers = amountTowers
		
		colorNum = 0
		colorAdd = -1
		for i in range(amountTowers):
			self.colorDict[i] = self.colors[colorNum]
			colorNum += colorAdd
			colorAdd *= -1
		
		self.width = 25
		self.towers = []
		for i in range(amountTowers):
			self.towers.append(Rectangle(Point(0,0), Point(50,50)))

	
	def generateColorDict(self):
		self.colorDict = {}
		colorNum = 0
		colorAdd = -1
		for i in range(self.amountTowers):
			self.colorDict[i] = self.colors[colorNum]
			colorNum += colorAdd
			colorAdd *= -1

		
	def drawList(self, lst, ascending=True):
		if ascending:
			lastRight = 25
			for i, number in enumerate(lst):
	
				self.towers[i].undraw()
				
				bottomLeft = lastRight
				tower = Rectangle(Point(bottomLeft, 0), Point(bottomLeft+self.width, number))
				self.towers[i] = tower
	
				color = self.colorDict[i]
				tower.setFill(color)
				tower.draw(self)
	
				lastRight = tower.getP2().getX()
		else:
			lastLeft = 775
			for i, number in enumerate(lst):
				
				self.towers[i].undraw()

				bottomRight = lastLeft
				tower = Rectangle(Point(bottomRight-self.width, 0), Point(bottomRight, number))
				self.towers[i] = tower

				color = self.colorDict[i]
				tower.setFill(color)
				tower.draw(self)

				lastLeft = tower.getP1().getX()

	def setColors(self, color1, color2):
		self.colors[0], self.colors[1] = color1, color2
		self.generateColorDict()
				