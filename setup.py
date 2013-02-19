# -*- coding: utf-8 -*-

from setuptools import find_packages
from setuptools import setup

LONG_DESCRIPTION = open('readme.rst').read()

setup(
    name='yelp',
    version='0.0.1',
    description="django-wysiwyg",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ],
    keywords='yelp,api,client',
    author="Garry Polley",
    author_email='garrympolley@gmail.com',
    url='https://github.com/pydanny/yelp-client',
    license='MIT',
    packages=find_packages(exclude=('test*',)),
    include_package_data=True,
    zip_safe=False
)
