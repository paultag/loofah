#!/usr/bin/env python

from setuptools import setup

long_description = open('README.md', 'r').read()

with open('requirements.txt') as f:
    install_requires = [l for l in f.read().splitlines()
                        if not l.startswith('#')]


setup(
    name="loofah",
    version="0.1",
    packages=[
        "loofah"
    ],
    author="Paul Tagliamonte",
    author_email="paultag@debian.org",
    long_description=long_description,
    install_requires=install_requires,
    scripts = ['bin/loofah-nuke',
               'bin/loofah-query',
               'bin/loofah-rebuild',
               'bin/loofah-update']
    description='debile helper to rebuild a set of existing packages',
    license="Expat",
    url="https://github.com/paultag/loofah",
    platforms=['any']
)
