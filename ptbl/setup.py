from setuptools import setup, find_packages
setup(
  name="ptbl",
  version="0.4",
  packages=find_packages(),
  package_data={
    'ptbl': ["bin/*", "data/*"],
  },
)
