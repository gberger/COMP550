class Vector(object):
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

	def dot(self, other):
		"""
		Dot product between two vectors.
		"""
		return self.x * other.x + self.y * other.y	

	def sub(self, other):
		"""
		Subtraction between two vectors.
		"""
		return Vector(other.x - self.x, other.y - self.y)

	def __eq__(self, other):
		"""
		Two vectors are equal if their X and Y are equal.
		"""
		return isinstance(other, self.__class__) and self.x == other.x and self.y == other.y

	def __ne__(self, other):
		return not self.__eq__(other)

class Point(Vector):
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

class Segment(object):
	def __init__(self, a, b):
		if not isinstance(a, Point) or not isinstance(b, Point):
			raise TypeError("Arguments to Segment must be two points")
		self.a = a
		self.b = b

	def vec(self):
		"""
		A line segment can be represented as the point A + the vector (B - A).
		"""
		return self.b.sub(self.a)

	def slope(self):
		"""
		Returns the slope of this segment, defined as dy/dx.
		Be aware that it can be infinite.
		"""
		try: 
			return float(self.a.y - self.b.y) / (self.a.x - self.b.x)
		except ZeroDivisionError:
			return float("inf")

	def is_parallel(self, other):
		return self.slope() == other.slope()

	def cross(self, other):
		"""
		Two segments cross if they share exactly one point that is not the 
		endpoint of either segment.
		If two segments are colinear, they are defined not to cross.
		Method derived from linear algebra.
		"""
		if not isinstance(other, Segment):
			raise TypeError("Must pass a Segment")

		if self.is_parallel(other):
			return False

		E = self.vec()
		F = other.vec()

		P = Vector(-E.y, E.x)
		h = float((self.a.sub(other.a)).dot(P)) / (F.dot(P))

		Q = Vector(-F.y, F.x)
		g = float((other.a.sub(self.a)).dot(Q)) / (E.dot(Q))

		# Using < instead of <= ensures that endpoints don't count as crossings		
		return 0 < h and h < 1 and 0 < g and g < 1

class ColoredSegment(Segment):
	def __init__(self, a, b, color):
		super(ColoredSegment, self).__init__(a, b)
		self.color = color