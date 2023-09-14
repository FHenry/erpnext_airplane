from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in airplane_mode/__init__.py
from airplane_mode import __version__ as version

setup(
	name="airplane_mode",
	version=version,
	description="Frappe Certification Process buildwithhussain",
	author="scopen.fr",
	author_email="florian.henry@scopen.fr",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
