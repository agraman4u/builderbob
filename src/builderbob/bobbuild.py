import sys

from builderbob.config import Config
from builderbob.utils.builder import Builder


def main(*args):
	args = sys.argv[1:]
	print("Running command with args:", args)

	config = Config()
	builder = Builder(config)
	builder.execute(args[0], *args[1:])

	print(config)
	return 0
