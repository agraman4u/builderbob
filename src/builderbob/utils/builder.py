import os
import subprocess

from builderbob.config import Config
from builderbob.constants import PACKAGE_BUILD_CONFIG_FILE


class Builder:
	def __init__(self, config: Config):
		self.config = config
		self.build_conf = Config(config_file=PACKAGE_BUILD_CONFIG_FILE)

	def _get_build_command(self, cmd, build_target, *args):
		assert cmd in self.build_conf.get("commands", required=True)[
			build_target], f"{cmd} not found for {build_target}"

		env = self.build_conf.get("build-system")[build_target]
		command = cmd
		try:
			command = self.build_conf.get("commandOverrides")[cmd][build_target]
		except KeyError:
			pass

		return " ".join([env, command, *args])

	def _get_build_system(self, build_target):
		return self.build_conf.get("build-system")[build_target]

	def _get_build_target(self):
		return self.config.get('target', required=True)

	def execute(self, cmd, *args):
		print("Building the package...")
		build_target = self._get_build_target()

		build_command = self._get_build_command(cmd, build_target, *args)
		print("Running command", build_command)
		result = subprocess.run(build_command, shell=True)
		if result.returncode != 0:
			raise Exception(f"Command {cmd} failed with code {result.returncode}")
		print("Build completed successfully")
		return result
