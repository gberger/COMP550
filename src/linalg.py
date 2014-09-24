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

	def compare(self, other):
		if not isinstance(other, self.__class__):
			raise TypeError("Can't compare")

		if self.x < other.x:
			return -1
		elif self.x > other.x:
			return 1
		elif self.y < other.y:
			return -1
		elif self.y > other.y:
			return 1
		else:
			return 0 

	def __lt__(self, other):
		return self.compare(other) < 0
	def __gt__(self, other):
		return self.compare(other) > 0
	def __eq__(self, other):
		return self.compare(other) == 0
	def __le__(self, other):
		return self.compare(other) <= 0
	def __ge__(self, other):
		return self.compare(other) >= 0
	def __ne__(self, other):
		return self.compare(other) != 0

class Point(Vector):
	def __init__(self, x, y):
		self.x = int(x)
		self.y = int(y)

class Flag(Point):
	def __init__(self, point, kind, parent):
		kind = kind.capitalize()
		if kind not in ['Start', 'Terminal']:
			raise TypeError("Valid kinds are 'Start' or 'Terminal'")
		if not isinstance(parent, Segment):
			raise TypeError("Parent must be a segment")
		if not isinstance(point, Point):
			raise TypeError("Must give a Point")

		self.x = point.x
		self.y = point.y
		self.point = point
		self.kind = kind
		self.parent = parent

	def slope(self):
		parent_slope = self.parent.slope()
		if self.kind == 'Start':
			return -parent_slope
		else:
			return parent_slope

	def color(self):
		return self.parent.color

	def compare(self, other):
		pt_cmp = self.point.compare(other.point)
		if pt_cmp != 0:
			return pt_cmp
		elif self.kind == 'Terminal' and other.kind == 'Start':
			return -1
		elif self.kind == 'Start' and other.kind == 'Terminal':
			return 1
		else:
			self_slope = self.slope()
			other_slope = other.slope()
			if self_slope < other_slope:
				return -1
			elif self_slope > other_slope:
				return 1
			elif self.kind == 'Start':
				if self.color() == 'Blue' and other.color() == 'Red':
					return -1
				elif self.color() == 'Red' and other.color() == 'Blue':
					return 1
			elif self.kind == 'Terminal':
				if self.color() == 'Blue' and other.color() == 'Red':
					return 1
				elif self.color() == 'Red' and other.color() == 'Blue':
					return -1
		raise ValueError("Overlapping lines of same color!")


class Segment(object):
	def __init__(self, a, b):
		if not isinstance(a, Point) or not isinstance(b, Point):
			raise TypeError("Arguments to Segment must be two points")

		if a > b:
			b, a = a, b

		self.a = Flag(a, 'Start', self)
		self.b = Flag(b, 'Terminal', self)

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
		color = color.capitalize()
		if color not in ['Red', 'Blue']:
			raise TypeError("Valid colors are 'Red' or 'Blue'")

		super(ColoredSegment, self).__init__(a, b)
		self.color = color