import os
import git


def _get_git_root(path=os.getcwd()):
	git_repo = git.Repo(path, search_parent_directories=True)
	git_root = git_repo.git.rev_parse("--show-toplevel")
	return git_root


CLIENT_ROOT_DIR = _get_git_root()
CLIENT_CONFIG_FILE = os.path.join(CLIENT_ROOT_DIR, "Bob")

PACKAGE_ROOT_DIR = _get_git_root(os.path.abspath(__file__))
PACKAGE_CONFIGURATION_DIR = os.path.join(PACKAGE_ROOT_DIR, "configuration")
PACKAGE_BUILD_CONFIG_FILE = os.path.join(PACKAGE_CONFIGURATION_DIR, "build_conf.json")
