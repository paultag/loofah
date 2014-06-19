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
    description='does some stuff with things & stuff',
    install_requires=install_requires,
    license="Expat",
    url="",
    platforms=['any']
)
