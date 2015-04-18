from triangulate import *
from triangle import *
from errors import *

img = loadImage('./images/hearken.jpg')

points = []
triangles = []

def setup():
	global points, triangles

	size(img.width/2, img.height/2)
	img.loadPixels()

	points = sorted(generateRandomPoints(200, width, height), key=lambda p: p.x)
	triangles = triangulate(points)

def draw():
	background(255)
	strokeWeight(2)

	# image(img, 0, 0) # Show/hide image

	for triangle in triangles:

		index = img.width * int(triangle.incenter.y) + int(triangle.incenter.x)
		c = img.pixels[index]
		fill(c)
		stroke(c)

		triangle.display()

	noLoop()
