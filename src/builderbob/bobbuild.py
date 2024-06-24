import sys

from builderbob.config import Config
from builderbob.utils.builder import Builder


def main():
	args = sys.argv[1:]
	if not args:
		args = ["build"]

	print("Running command with args:", args)

	config = Config()
	builder = Builder(config)
	builder.execute(args[0], *args[1:])
	return 0
