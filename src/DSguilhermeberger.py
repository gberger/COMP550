import sys

from linalg import *
import read_segments
from sortlist import sortlist

def DSguilhermeberger(filename):
	"""
	Input: a set of (supposedly) non-touching blue segments 
	Output: True iff they are non-touching -- share absolutely no points.
	"""

	reds, blus, expected = read_segments.read(filename)

	bot_sentinel = ColoredSegment(Point(MIN_COORD-1, MIN_COORD-1), Point(MAX_COORD+1, MIN_COORD-1), 'Blue')
	top_sentinel = ColoredSegment(Point(MIN_COORD-1, MAX_COORD+1), Point(MAX_COORD+1, MAX_COORD+1), 'Blue')

	blu_start_flags = [seg.a for seg in blus]
	blu_terminal_flags = [seg.b for seg in blus]

	flags = blu_start_flags + blu_terminal_flags

	# This list is ordered by the flag sorting conditions defined on SI3
	flags = sorted(flags)

	# This list is ordered by the Y coordinate of the Start flag
	sweep = sortlist([], lambda segment: segment.a.y)
	sweep.insert(bot_sentinel)
	sweep.insert(top_sentinel)

	# By iterating through `flags`, we are effectively sweeping a vertical line from left to right
	for flag in flags:
		if flag.kind == 'Start':
			# If we found a Start flag, we add its segment to the active list
			# It may cross the segment before or after it
			sweep.insert(flag.parent)
			index = sweep.index(flag.parent)
			if sweep[index-1].cross(sweep[index]) or sweep[index].cross(sweep[index+1]):
				return False

		else:
			# If we found a Terminal flag, we remove its segment from the active list
			# Now, its remaining neighbors may cross
			index = sweep.index(flag.parent)
			if sweep[index-1].cross(sweep[index+1]):
				return False
			sweep.remove(flag.parent) 

	return True

if __name__ == '__main__':
	filename = sys.argv[1]
	if DSguilhermeberger(filename):
		print("VERIFIED")
