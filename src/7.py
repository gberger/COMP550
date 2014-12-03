import sys, re

from linalg import *
import read_segments

def assign_sentinels(arr, color):
	bot_sentinel = ColoredSegment(Point(MIN_COORD-1, MIN_COORD-1), Point(MAX_COORD+1, MIN_COORD-1), color)
	top_sentinel = ColoredSegment(Point(MIN_COORD-1, MAX_COORD+1), Point(MAX_COORD+1, MAX_COORD+1), color)
	bot_sentinel.num = 0
	top_sentinel.num = len(arr)+1
	arr.insert(0, bot_sentinel)
	arr.append(top_sentinel)

PATTERN_FLAGS = re.compile('\s*(\d+)\s*([BR])([ST])')
def parse_sorted_flag_line(line):
	m = PATTERN_FLAGS.match(line)
	if m is None:
		raise 'Badly formed SORTED FLAGS file'
	index, color, kind = m.groups()
	index = int(index)
	return index, color, kind

def retrieve_flag(index, color, kind, reds, blus):
	arr = reds if color == 'R' else blus
	segment = arr[index]
	if kind == 'S':
		return segment.a
	else:
		return segment.b

def sorted_flags(filename, reds, blus):
	with open(filename, 'r') as f:
		arr = []
		for line in f:
			index, color, kind = parse_sorted_flag_line(line)
			flag = retrieve_flag(index, color, kind, reds, blus)
			arr.append(flag)
	return arr

PATTERN_AB = re.compile('\s*(\d+)\s*([BR])([ST])\s*(\d+)\s*(\d+)\s*(\d+)\s*(\d+)')
def parse_above_below_line(line):
	m = PATTERN_AB.match(line)
	if m is None:
		raise 'Badly formatted ABOVE BELOW file'
	index, color, kind, sb, sa, ob, oa = m.groups()
	index = int(index)
	sb = int(sb)
	sa = int(sa)
	ob = int(ob)
	oa = int(oa)
	return index, color, kind, sb, sa, ob, oa

def assign_above_below(filename, reds, blus):
	with open(filename, 'r') as f:
		for line in f:
			index, color, kind, sb, sa, ob, oa = parse_above_below_line(line)
			flag = retrieve_flag(index, color, kind, reds, blus)
			if color == 'R':
				flag.sb = reds[sb]
				flag.sa = reds[sa]
				flag.ob = blus[ob]
				flag.oa = blus[oa]
			else:
				flag.sb = blus[sb]
				flag.sa = blus[sa]
				flag.ob = reds[ob]
				flag.oa = reds[oa]


if __name__ == '__main__':
	reds, blus, expected = read_segments.read(sys.argv[1])
	assign_sentinels(reds, 'Red')
	assign_sentinels(blus, 'Blue')
	assign_above_below(sys.argv[3], reds, blus)
	flags = sorted_flags(sys.argv[2], reds, blus)

	print flags