from setuptools import setup, find_packages

setup(
    name = 'bsvxpy',
    version = '0.1',
    packages = find_packages(exclude='tests'),
    long_description = open('README.md').read()
)