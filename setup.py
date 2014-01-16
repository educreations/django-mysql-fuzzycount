#!/usr/bin/env python

import os
import sys

from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py register sdist upload')
    os.system('python setup.py register bdist_wheel upload')
    sys.exit()


with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name="django-mysql-fuzzycount",
    version="0.2",
    description="Approximate query counts for MySQL and Django.",
    license="MIT",
    keywords="mysql orm django",
    author="Chris Streeter",
    author_email="chris@educreations.com",
    url="https://github.com/educreations/django-mysql-fuzzycount",
    long_description=readme,
    packages=["mysql_fuzzycount"],
    package_dir={"mysql_fuzzycount": "mysql_fuzzycount"},
    install_requires=[
        "django >= 1.5",
        "django-model-utils >= 1.4.0",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development',
    ],
)
