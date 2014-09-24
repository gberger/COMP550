import sys
from linalg import *
import read_segments

def BFguilhermeberger():
	"""
	Given a file representing red and blue segments,
	and an expected number of crossings between red and blue
	segments, verify that this expected number is correct.
	"""

	filename = sys.argv[1]
	reds, blus, expected = read_segments.read(filename)
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
