import sys
from linalg import *

def read_segment(str, color):
	ax, ay, bx, by = map(int, str.strip().split(' '))
	return ColoredSegment(Point(ax, ay), Point(bx, by), color)

def BFguilhermeberger():
	filename = sys.argv[1]
	f = open(filename, 'r')
	first = next(f)

	nreds, nblues, expected = map(int, first.strip().split())

	reds = [read_segment(next(f), 'red') for i in range(nreds)]
	blus = [read_segment(next(f), 'blue') for i in range(nblues)]

	f.close()

	actual = 0

	for red in reds:
		for blu in blus:
			if red.cross(blu):
				actual += 1

	return (actual == expected, actual, expected)


if __name__ == '__main__':
	verified, actual, expected = BFguilhermeberger()
	if verified:
		print("VERIFIED")
	else:
		print("FAIL")
		print("EXPECTED %d" % expected)
		print("ACTUAL   %d" % actual)
