# box = [L, W, H, Edges]
from msilib.schema import Class
from operator import length_hint


boxes = []

class Box:
    length = 0
    width = 0
    height = 0
    edges = []

    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def canStackOn(self, boxB):
        return self.length < boxB.length and self.width < boxB.width

boxes.append(Box(4, 5, 3))
boxes.append(Box(2, 3, 2))
boxes.append(Box(3, 6, 2))
boxes.append(Box(1, 5, 4))
boxes.append(Box(2, 4, 1))
boxes.append(Box(1, 2, 2))


boxes.sort(key=lambda x: x.length * x.width, reverse=True)
values = {}
maxHeight = 0
for box in boxes:
    values[box] = box.height
for i in range(len(boxes)):
    for j in range(i):
        if boxes[i].canStackOn(boxes[j]):
            newHeight = boxes[i].height + values[boxes[j]]
            if newHeight > values[boxes[i]]:
                values[boxes[i]] = newHeight
            if newHeight > maxHeight:
                maxHeight = newHeight
                

print(maxHeight)