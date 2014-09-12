from linalg import *

def read_segment(str):
	ax, ay, bx, by = map(int, str.strip().split(' '))
	return Segment(Point(ax, ay), Point(bx, by))

def BFguilhermeberger():
	f = open('T1guilhermeberger.txt', 'r')
	first = next(f)

	nreds, nblues, expected = map(int, first.strip().split())

	reds = [read_segment(next(f)) for i in range(nreds)]
	blus = [read_segment(next(f)) for i in range(nblues)]

	f.close()

	actual = 0

	for red in reds:
		for blu in blus:
			if red.cross(blu):
				actual += 1

	return actual == expected


if __name__ == '__main__':
	if BFguilhermeberger() == True:
		print("VERIFIED")
