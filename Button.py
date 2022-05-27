# button.py
from graphics import *


class Button:
    def __init__(self, win, center, width, height, label, color='white'):
        self.color = color
        w, h = width / 2.0, height / 2.0
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
        self.win = win

    def getCenter(self):
        return self.rect.getCenter()

    def clicked(self, p):
        return (self.active and self.xmin <= p.getX() <= self.xmax
                and self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def setLabel(self, label):
    	self.label.setText(label)
    	self.redraw()

    def setLabelSize(self, size):
        self.label.setSize(size)

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.rect.setFill(self.color)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False

    def setFill(self, color):
        self.rect.setFill(color)

    def undraw(self):
        self.rect.undraw()
        self.label.undraw()

    def draw(self):
        self.rect.draw(self.win)
        self.label.draw(self.win)

    def redraw(self):
    	self.undraw()
    	self.draw()
