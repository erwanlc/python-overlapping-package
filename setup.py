from setuptools import setup

setup(name='proj',
      version=1.0,
	  author='Erwan Le Covec'
      description="Python package for data overlapping",
      packages=['proj'],
      test_suite = 'tests',
      #include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/proj-run'],
      zip_safe=False)

