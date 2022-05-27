import json
from random import randint
import sys
def generateLsts(name, length):
	lst = []
	file = "C:\\Users\\Joseph Stambaugh\\Dropbox\\My PC (UnknownDevice)\\Desktop\\sorting_algorithms\\lists\\lists.json"
	for i in range(length):
		lst.append(randint(1, length))

	with open(file, "r") as f:
		data = json.loads(f.read())
	data[str(name)].append(lst)
	with open(file, "w") as f:
		f.write(json.dumps(data))