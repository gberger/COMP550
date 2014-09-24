import sys
from linalg import *
import read_segments

def SFguilhermeberger():
	"""
	Given a file representing red and blue segments,
	sort the implicit flags and print them to stdout.
	"""

	filename = sys.argv[1]
	reds, blus, expected = read_segments.read(filename)

	red_start_flags = [seg.a for seg in reds]
	red_terminal_flags = [seg.b for seg in reds]
	blu_start_flags = [seg.a for seg in blus]
	blu_terminal_flags = [seg.b for seg in blus]

	flags = red_start_flags + red_terminal_flags + blu_start_flags + blu_terminal_flags
	flags = sorted(flags)

	for flag in flags:
		print flag.parent.num, flag.color(), flag.kind

if __name__ == '__main__':
	SFguilhermeberger()