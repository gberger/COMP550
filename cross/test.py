from linalg import *
import unittest

class TestLinearAlgebra(unittest.TestCase):

	def test_eq(self):
		a = Vector(1, 2)
		b = Vector(1.0, 2.0)

		self.assertEqual(a, b)

	def test_ne(self):
		a = Vector(1, 2)
		b = Vector(10, 555)

		self.assertNotEqual(a, b)

	def test_dot(self):
		a = Vector(-6, 8)
		b = Vector(5, 12)

		self.assertEqual(a.dot(b), 66)
		
	def test_dot2(self):
		a = Vector(-60, 80)
		b = Vector(50, 120)

		self.assertEqual(a.dot(b), 6600)
		
	def test_sub_vecs(self):
		a = Vector(-6, 8)
		b = Vector(5, 12)

		c = Vector(11, 4)

		self.assertEqual(a.sub(b), c)

	def test_sub_points(self):
		a = Point(-6, 8)
		b = Point(5, 12)

		c = Vector(11, 4)

		self.assertEqual(a.sub(b), c)

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

if __name__ == '__main__':
	unittest.main()