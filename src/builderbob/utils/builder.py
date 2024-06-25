import os
import subprocess

from builderbob.config import Config
from builderbob.constants import PACKAGE_BUILD_CONFIG_FILE, CLIENT_ROOT_DIR


class Builder:
	def __init__(self, config: Config):
		self.client_config = config
		self.build_conf = Config(config_file=PACKAGE_BUILD_CONFIG_FILE)

	def _get_build_command(self, cmd, *args):
		if self._get_build_system() not in self.build_conf.get("build-system").keys():
			return self.get_custom_build_command(cmd, *args)
		assert cmd in self.build_conf.get("commands", required=True)[
			self._get_build_system()], f"{cmd} not found for {self._get_build_system()}"
		build_system = self._get_build_system()
		env = self.build_conf.get("build-system")[build_system]
		command = cmd
		try:
			command = self.build_conf.get("commandOverrides")[cmd][build_system]
		except KeyError:
			pass

		return " ".join([env, command, *args])

	def _get_build_system(self):
		return self.client_config.get("build-system")

	def _get_build_target(self):
		return self.client_config.get('target', required=True)

	def execute(self, cmd, *args):
		print("Building the package...")

		is_valid, errors = self._is_valid_client_config()
		assert is_valid, errors

		build_command = self._get_build_command(cmd, *args)
		print("Running command", build_command)
		result = subprocess.run(build_command, shell=True)
		if result.returncode != 0:
			raise Exception(f"Command {cmd} failed with code {result.returncode}")
		print("Build completed successfully")
		return result

	def _build_validation_clause(self, condition, error_msg):
		return lambda: (-1, error_msg) if not condition() else (0, "")

	def _is_valid_client_config(self):
		checks = [
			self._build_validation_clause(
				lambda: self._get_build_system() in self.build_conf.get("supportedLibraries")[
					self._get_build_target()] or os.path.exists(self.get_custom_build_path()),
				f"Library '{self._get_build_target()}' is not supported/found for build system '{self._get_build_system()}'")
		]
		validation_res = list(filter(lambda x: x[0] != 0, map(lambda x: x(), checks)))
		if not validation_res:
			return True, []
		return False, list(zip(*validation_res))[0]

	def get_custom_build_command(self, cmd, *args):
		return " ".join([self.get_custom_build_path(), cmd, *args])

	def get_custom_build_path(self):
		return os.path.join(CLIENT_ROOT_DIR, "bin", "build-scripts", self._get_build_system())
