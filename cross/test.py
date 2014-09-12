from linalg import *
import unittest

class TestVector(unittest.TestCase):
	def test_eq(self):
		a = Vector(1, 2)
		b = Vector(1.0, 2.0)
		self.assertEqual(a, b)

	def test_ne(self):
		a = Vector(1, 2)
		b = Vector(10, 555)
		self.assertNotEqual(a, b)

	def test_lt_x(self):
		a = Vector(1, 2)
		b = Vector(3, 4)
		self.assertTrue(a < b)

	def test_lt_y(self):
		a = Vector(1, 2)
		b = Vector(1, 4)
		self.assertTrue(a < b)

	def test_gt_x(self):
		a = Vector(1, 2)
		b = Vector(3, 4)
		self.assertTrue(b > a)

	def test_gt_y(self):
		a = Vector(1, 2)
		b = Vector(1, 4)
		self.assertTrue(b > a)

	def test_dot(self):
		a = Vector(-6, 8)
		b = Vector(5, 12)
		self.assertEqual(a.dot(b), 66)
		
	def test_dot_2(self):
		a = Vector(-60, 80)
		b = Vector(50, 120)
		self.assertEqual(a.dot(b), 6600)
		
	def test_sub(self):
		a = Vector(-6, 8)
		b = Vector(5, 12)
		c = Vector(11, 4)
		self.assertEqual(a.sub(b), c)

class TestPoint(unittest.TestCase):
	def test_sub(self):
		a = Point(-6, 8)
		b = Point(5, 12)
		c = Vector(11, 4)
		self.assertEqual(a.sub(b), c)

class TestFlag(unittest.TestCase):
	def test_init(self):
		a = Point(-6, 8)
		b = Point(5, 12)
		s = Segment(a, b)
		self.assertRaises(TypeError, Flag, (None, 'start', s))
		self.assertRaises(TypeError, Flag, (a, 'blablabl', s))
		self.assertRaises(TypeError, Flag, (a, 'start', None))

	def test_compare_kind(self):
		# terminal < start
		a = Point(1, 1)
		b = Point(2, 2)
		c = Point(3, 3)
		s = ColoredSegment(a, b, 'blue')
		t = ColoredSegment(b, c, 'blue')
		self.assertTrue(s.b < t.a)

	def test_compare_slope(self):
		# compare slope
		a = Point(1, 1)
		b = Point(2, 2)
		d = Point(2, 3)
		s = ColoredSegment(a, b, 'blue')
		r = ColoredSegment(a, d, 'blue')
		self.assertTrue(s.a > r.a)

	def test_compare_color(self):
		a = Point(1, 1)
		b = Point(2, 2)
		s = ColoredSegment(a, b, 'blue')
		u = ColoredSegment(a, b, 'red')
		# blue start < red start
		self.assertTrue(s.a < u.a)
		# red terminal < blue terminal
		self.assertTrue(u.b < s.b)

	def test_compare_overlapping(self):
		a = Point(1, 1)
		b = Point(2, 2)
		c = Point(3, 3)
		s = ColoredSegment(a, b, 'blue')
		r = ColoredSegment(a, c, 'blue')
		self.assertRaises(ValueError, s.a.compare, r.a)

	def test_slope(self):
		a = Point(1, 1)
		b = Point(2, 2)
		s = Segment(a, b)

		self.assertEqual(s.a.slope(), -1.0)
		self.assertEqual(s.b.slope(),  1.0)


class TestSegment(unittest.TestCase):
	def test_cross_1(self):
		a = Point(0, 0)
		b = Point(1, 1)
		c = Point(0, 1)
		d = Point(1, 0)
		r = Segment(a, b)
		s = Segment(c, d)
		self.assertTrue(r.cross(s))

	def test_cross_2(self):
		a = Point(0, 0)
		b = Point(1, 1)
		c = Point(1, 1)
		d = Point(0, 2)
		r = Segment(a, b)
		s = Segment(c, d)
		self.assertFalse(r.cross(s))

	def test_cross_3(self):
		a = Point(0, 0)
		b = Point(1, 1)
		c = Point(0, 1)
		d = Point(1, 2)
		r = Segment(a, b)
		s = Segment(c, d)
		self.assertFalse(r.cross(s))

	def test_cross_4(self):
		a = Point(0, 0)
		b = Point(1, 1)
		c = Point(2, 2)
		d = Point(3, 5)
		r = Segment(a, b)
		s = Segment(c, d)
		self.assertFalse(r.cross(s))

class TestColoredSegment(unittest.TestCase):
	def test_init(self):
		a = Point(-6, 8)
		b = Point(5, 12)
		self.assertRaises(TypeError, ColoredSegment, (a, b, 'blabla'))

if __name__ == '__main__':
	unittest.main()