import os
from setuptools import setup, find_packages

package_dir = os.path.join("PyFlow", "Packages")
packages = find_packages(package_dir)
packages = [os.path.join(package_dir, pkg) for pkg in packages]


setup(name='pyflow.pyrr',
      version="0.0.1",
      packages=packages,
      maintainer="TODO",
      maintainer_email="TODO",
      url="https://github.com/wonderworks-software/PyFlowPyrr",
      description="pyrr nodes for pyflow",
      install_requires=['numpy'], 
      include_package_data=True)
