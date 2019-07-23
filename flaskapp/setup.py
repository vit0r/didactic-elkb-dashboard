"""Setup app from setup.cfg
"""

from setuptools import setup, find_packages

setup(
    packages=find_packages(exclude=['tests']),
    install_requires=['flask==1.1.1']
)