from setuptools import setup, find_packages
import io

# List all of your Python package dependencies in the
# requirements.txt file


def readfile(filename, split=False):
    with io.open(filename, encoding="utf-8") as stream:
        if split:
            return stream.read().split("\n")
        return stream.read()

readme = readfile("README.rst", split=True)[3:]  # skip title
requires = readfile("requirements.txt", split=True)
software_license = readfile("LICENSE")

setup(name='mapclientplugins.heartsurfacesegmenterstep',
      version='0.1.0',
      description='',
      long_description=''.join(readme) + software_license,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
      ],
      author='Hugh Sorby',
      author_email='',
      url='',
      license='APACHE',
      packages=find_packages(exclude=['ez_setup',]),
      namespace_packages=['mapclientplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      )
