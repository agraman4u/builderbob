import os
import git


def _get_git_root():
	git_repo = git.Repo(os.getcwd(), search_parent_directories=True)
	git_root = git_repo.git.rev_parse("--show-toplevel")
	return git_root


ROOT_DIR = _get_git_root()  # This is your Project Root
CLIENT_CONFIG_FILE = os.path.join(ROOT_DIR, "Bob")
PACKAGE_CONFIGURATION_DIR = os.path.join(ROOT_DIR, "configuration")
PACKAGE_BUILD_CONFIG_FILE = os.path.join(PACKAGE_CONFIGURATION_DIR, "build_conf.json")
