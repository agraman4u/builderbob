import os
import subprocess

from builderbob.config import Config
from builderbob.constants import PACKAGE_BUILD_CONFIG_FILE


class Builder:
	def __init__(self, config: Config):
		self.config = config
		self.build_conf = Config(config_file=PACKAGE_BUILD_CONFIG_FILE)

	def _exec_build_command(self, cmd, *args):
		build_target = self.config.get('target', required=True)
		build_command = self.build_conf.get(cmd)[build_target]
		print("Running command", build_command)
		result = subprocess.run(build_command, shell=True)
		if result.returncode != 0:
			raise Exception(f"Command {cmd} failed with code {result.returncode}")
		return result

	def build(self):
		# Simulate building process
		print("Building the package...")
		# Implement your build logic here
		res = self._exec_build_command("build")
		print("Build completed successfully")
		return res

	def release(self):
		# Simulate building process
		print("Building the package release...")
		# Implement your build logic here
		res = self._exec_build_command("release")
		print("Build completed successfully")
		return res
