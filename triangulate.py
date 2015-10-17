from triangle import *

def generateRandomPoints(number, width, height):
	points = []
	for i in xrange(number):
		points.append(PVector(int(random(width)), int(random(height))))
	return points

def superTriangle(points):

	xMin = float('inf')
	yMin = float('inf')

	xMax = float('-inf')
	yMax = float('-inf')

	for point in points:
		if point.x < xMin:
			xMin = point.x
		if point.x > xMax:
			xMax = point.x
		if point.y < yMin:
			yMin = point.y
		if point.y > yMax:
			yMax = point.y

	dx = xMax - xMin
	dy = yMax - yMin
	dMax = max(dx, dy)

	xMid = xMin + 0.5 * dx
	yMid = yMin + 0.5 * dy

	return Triangle(
			PVector( xMid - 10 * dMax, yMid - dMax ), 
			PVector( xMid, yMid + 10 * dMax ), 
			PVector( xMid + 10 * dMax, yMid - dMax )
		)

def superTriangle(width, height):

	return Triangle(
			PVector( - 2 * width, - height ),
			PVector( 3 * width, - height),
			PVector( width / 2, 3 * height )
		)

def dedupe(edges):
	seen = set()
	duplicates = set()
	for e in edges:

		if e in seen:
			duplicates.add(e)
			duplicates.add((e[1], e[0]))

		seen.add(e)
		seen.add((e[1], e[0]))

	return [ e for e in edges if e not in duplicates ]

def triangulate(points):
	triangles = set()
	super = superTriangle(width, height)
	stroke(255, 0, 0)
	stroke(0)
	triangles.add(super)

	for point in points:
		edges = []

		for triangle in list(triangles):
			if triangle.circumcircleContains(point):
				triangles.remove(triangle)
				edges += triangle.toEdges()	

		edges = dedupe(edges)

		for edge in edges:
			triangles.add(Triangle(point, edge[0], edge[1]))

	triangles = [t for t in triangles if t.toPoints().isdisjoint(super.toPoints())]

	return triangles