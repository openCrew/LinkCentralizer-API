# -*- coding: utf-8 -*-

# Third
from setuptools import find_packages, setup

__version__ = '0.1.0'
__description__ = 'Link centralizer'
__long_description__ = 'This is an API to Flask '

__author__ = 'openCrew'
__author_email__ = ''

setup(
    name='LinkCentralizer',
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=find_packages(),
    license='MIT',
    description=__description__,
    long_description=__long_description__,
    url='https://github.com/openCrew/LinkCentralizer.git',
    keywords='API, CENTRALIZER',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
    ],
)