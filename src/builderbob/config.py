import json
import os

from builderbob.constants import CLIENT_CONFIG_FILE


class Config:
	def __init__(self, config_file=CLIENT_CONFIG_FILE):
		self.config_file = config_file
		self.config = self.load_config()
		print("Loaded", config_file, self.config)

	def load_config(self):
		if not os.path.exists(self.config_file):
			return {}
		with open(self.config_file, 'r') as file:
			return json.load(file)

	def get(self, key, default=None, required=False):
		val = self.config.get(key, default)
		if required:
			assert val, f"Value cannot be None. Meta field missing: {key}"
		return val
