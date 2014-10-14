import sys, os

from linalg import *
import read_segments

class Blackhole(object):
    def write(self, string):
        pass
stdout = sys.stdout
sys.stdout = Blackhole()
from bintrees import AVLTree
sys.stdout = stdout

def ABguilhermeberger(reds, blus):
	"""
	Input: red and blue segments with no red/red or blue/blue crossings, and no endpoints inside segments 
	Output: For each flag, the segment above and below of the same and the opposite color.
	"""
	red_bot_sentinel = ColoredSegment(Point(MIN_COORD-1, MIN_COORD-1), Point(MAX_COORD+1, MIN_COORD-1), 'Red')
	red_top_sentinel = ColoredSegment(Point(MIN_COORD-1, MAX_COORD+1), Point(MAX_COORD+1, MAX_COORD+1), 'Red')
	red_bot_sentinel.num = 0
	red_top_sentinel.num = len(reds)+1

	blu_bot_sentinel = ColoredSegment(Point(MIN_COORD-1, MIN_COORD-1), Point(MAX_COORD+1, MIN_COORD-1), 'Blue')
	blu_top_sentinel = ColoredSegment(Point(MIN_COORD-1, MAX_COORD+1), Point(MAX_COORD+1, MAX_COORD+1), 'Blue')
	blu_bot_sentinel.num = 0
	blu_top_sentinel.num = len(blus)+1

	blu_start_flags = [seg.a for seg in blus]
	blu_termi_flags = [seg.b for seg in blus]

	red_start_flags = [seg.a for seg in reds]
	red_termi_flags = [seg.b for seg in reds]

	red_flags = red_start_flags + red_termi_flags
	blu_flags = blu_start_flags + blu_termi_flags

	# Lists ordered by the flag sorting conditions defined on SI3
	red_flags = sorted(red_flags)
	blu_flags = sorted(blu_flags)
	flags = sorted(red_flags + blu_flags)

	# This list is ordered by the Y coordinate of the Start flag
	red_sweep = AVLTree()
	red_sweep.insert(red_bot_sentinel, red_bot_sentinel)
	red_sweep.insert(red_top_sentinel, red_top_sentinel)

	blu_sweep = AVLTree()
	blu_sweep.insert(blu_bot_sentinel, blu_bot_sentinel)
	blu_sweep.insert(blu_top_sentinel, blu_top_sentinel)

	def get_same_sweep(flag):
		if flag.color() == 'Blue':
			return blu_sweep
		else:
			return red_sweep

	def get_other_sweep(flag):
		if flag.color() == 'Red':
			return blu_sweep
		else:
			return red_sweep

	# By iterating through `flags`, we are effectively sweeping a vertical line from left to right
	for flag in flags:

		segment = flag.parent
		same_sweep = get_same_sweep(flag)
		other_sweep = get_other_sweep(flag)

		if flag.kind == 'Start':
			same_sweep.insert(segment, segment)
			flag.sb = same_sweep.prev_item(segment)[0].num
			flag.sa = same_sweep.succ_item(segment)[0].num
		else:
			flag.sb = segment.num
			flag.sa = segment.num
			same_sweep.remove(segment)

		other_sweep.insert(segment, segment)
		flag.ob = other_sweep.prev_item(segment)[0].num
		flag.oa = other_sweep.succ_item(segment)[0].num
		other_sweep.remove(segment)

	return red_flags, blu_flags

if __name__ == '__main__':
	filename = sys.argv[1]
	times = int(sys.argv[2]) if len(sys.argv) >= 3 else 1

	reds, blus, expected = read_segments.read(filename)
	red_flags, blu_flags = ABguilhermeberger(reds, blus)

	for i in range(times-1):
		ABguilhermeberger(reds, blus)

	for flag in red_flags:
		print "%dR%s %d %d %d %d" % (flag.num(), flag.kind[0], flag.sb, flag.sa, flag.ob, flag.oa)
	for flag in blu_flags:
		print "%dB%s %d %d %d %d" % (flag.num(), flag.kind[0], flag.sb, flag.sa, flag.ob, flag.oa)