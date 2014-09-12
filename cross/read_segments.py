from linalg import *

def read_segment(str, color):
	ax, ay, bx, by = map(int, str.strip().split())
	return ColoredSegment(Point(ax, ay), Point(bx, by), color)

def read(filename):
	f = open(filename, 'r')
	first = next(f)

	nreds, nblues, expected = map(int, first.strip().split())

	reds = [read_segment(next(f), 'red') for i in range(nreds)]
	blus = [read_segment(next(f), 'blue') for i in range(nblues)]

	f.close()

	for idx, red in enumerate(reds):
		red.num = idx+1
	for idx, blu in enumerate(blus):
		blu.num = idx+1

	return (reds, blus, expected)