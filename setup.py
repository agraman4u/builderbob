from setuptools import setup, find_packages


def read_requirements(file):
	with open(file, 'r') as f:
		return f.read().splitlines()


# Reading dependencies from requirements.txt
requirements = read_requirements('requirements.txt')

setup(
	name='builderbob',
	version='0.1',
	packages=find_packages(where="src"),
	package_dir={'': 'src'},
	author='Aman Agrawal',
	author_email='agraman4u@gmail.com',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	install_requires=requirements,
	entry_points={
		'console_scripts': [
			'bob-build=builderbob.bobbuild:main',
		],
	},
	description='A description of your package',
	url='https://github.com/agraman4u/builderbob',
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
	package_data={
		'': ['*.txt', '*.rst'],
		'builderbob': ['data/*', "configuration/*", "*.txt"],
	},
	python_requires='>=3.10',
	zip_safe=False
)
