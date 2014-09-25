import sys

from linalg import *
import read_segments
from bintree import BinaryTree

def DSguilhermeberger(blus):
	"""
	Input: a set of (supposedly) non-touching blue segments 
	Output: True iff they are non-touching -- share absolutely no points.
	"""

	bot_sentinel = ColoredSegment(Point(MIN_COORD-1, MIN_COORD-1), Point(MAX_COORD+1, MIN_COORD-1), 'Blue')
	top_sentinel = ColoredSegment(Point(MIN_COORD-1, MAX_COORD+1), Point(MAX_COORD+1, MAX_COORD+1), 'Blue')

	bot_sentinel.num = float("-inf")
	top_sentinel.num = float("inf")

	blu_start_flags = [seg.a for seg in blus]
	blu_terminal_flags = [seg.b for seg in blus]

	flags = blu_start_flags + blu_terminal_flags

	# This list is ordered by the flag sorting conditions defined on SI3
	flags = sorted(flags)

	# This list is ordered by the Y coordinate of the Start flag
	sweep = BinaryTree()
	sweep.insert(bot_sentinel, bot_sentinel.num)
	sweep.insert(top_sentinel, top_sentinel.num)

	# By iterating through `flags`, we are effectively sweeping a vertical line from left to right
	for flag in flags:
		segment = flag.parent

		if flag.kind == 'Start':
			# If we found a Start flag, we add its segment to the active list
			# It may cross the segment before or after it
			sweep.insert(segment, segment.num)

			prev = sweep.predecessor_to(segment, segment.num)
			succ = sweep.successor_to(segment, segment.num)

			if prev.cross(segment) or segment.cross(succ):
				return False

		else:
			# If we found a Terminal flag, we remove its segment from the active list
			# Now, its remaining neighbors may cross
			prev = sweep.predecessor_to(segment, segment.num)
			succ = sweep.successor_to(segment, segment.num)

			if prev.cross(succ):
				return False
			sweep.remove(segment)

	return True

if __name__ == '__main__':
	filename = sys.argv[1]
	times = int(sys.argv[2]) if len(sys.argv) >= 3 else 1

	reds, blus, expected = read_segments.read(filename)

	for i in range(times):
		verified = DSguilhermeberger(blus)

	if verified:
		print("VERIFIED")
