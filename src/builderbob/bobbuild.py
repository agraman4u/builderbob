import argparse
import json

from builderbob.config import Config
from builderbob.utils.builder import Builder


def main():
	parser = argparse.ArgumentParser(description="Build and release packages")
	parser.add_argument('command', choices=['build', 'release'], help="Command to execute")
	args = parser.parse_args()
	print("Running command with args:", args)

	config = Config()
	builder = Builder(config)

	if args.command == 'build':
		builder.build()
	elif args.command == 'release':
		builder.release()

	print(config)
	return 0
