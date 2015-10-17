from triangulate import *
from triangle import *

img = loadImage('./images/hearken.jpg')

points = []
triangles = []
n = 300
showImage = True
transparent = False

def setup():
	global points, triangles, n

	size(img.width, img.height)
	img.loadPixels()

	points = sorted(generateRandomPoints(n, width, height), key=lambda p: p.x)
	triangles = triangulate(points)

	noStroke()

def draw():
	background(255)

	if showImage:
		image(img, 0, 0)

	for triangle in triangles:

		index = img.width * int(triangle.incenter.y) + int(triangle.incenter.x)
		c = img.pixels[index]
		fill(c, 127 if transparent else 255)

		triangle.display()
	noLoop()
