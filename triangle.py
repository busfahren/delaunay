class Triangle:

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

        # http://www.mathopenref.com/trianglecircumcircle.html
        a, b, c = self.toLengths()
        self.radSq = sq(a * b * c) / float((a+b+c)*(b+c-a)*(c+a-b)*(a+b-c))

        # http://en.wikipedia.org/wiki/Circumscribed_circle#Circumcenter_coordinates
        d = 2 * (A.x * (B.y - C.y) + B.x * (C.y - A.y) + C.x * (A.y - B.y))
        circumcenterX = ((sq(A.x) + sq(A.y)) * (B.y - C.y) \
                        + (sq(B.x) + sq(B.y)) * (C.y - A.y) \
                        + (sq(C.x) + sq(C.y)) * (A.y - B.y)) \
                        /d
        circumcenterY = ((sq(A.x) + sq(A.y)) * (C.x - B.x) \
                        + (sq(B.x) + sq(B.y)) * (A.x - C.x) \
                        + (sq(C.x) + sq(C.y)) * (B.x - A.x)) \
                        /d

        self.circumcenter = PVector(circumcenterX, circumcenterY)

        # http://de.wikipedia.org/wiki/Inkreis
        self.incenter = PVector.div((PVector.mult(A, a) + PVector.mult(B, b) + PVector.mult(C, c)), a + b + c)

    def toString(self):
        return "Points: (%d, %d) (%d, %d) (%d, %d)" \
        % (self.A.x, self.A.y, self.B.x, self.B.y, self.C.x, self.C.y)

    def toPoints(self):
        return set([self.A, self.B, self.C])

    def toEdges(self):
        return [(self.B, self.C), (self.C, self.A), (self.A, self.B)]

    def toLengths(self):
        return [(e[0] - e[1]).mag() for e in self.toEdges()]

    def circumcircleContains(self, point):
        return (point - self.circumcenter).magSq() < self.radSq

    def display(self):
        triangle(self.A.x, self.A.y, self.B.x, self.B.y, self.C.x, self.C.y)