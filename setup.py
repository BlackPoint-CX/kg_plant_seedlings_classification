#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

setup_requirements = [
    # TODO(BlackPoint-CX): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='kg_plant_seedlings_classification',
    version='0.1.0',
    description="Kaggle Competition - Plant Seedlings Classification",
    long_description=readme + '\n\n' + history,
    author="BlackPoint",
    author_email='chenxiang0815@gmail.com',
    url='https://github.com/BlackPoint-CX/kg_plant_seedlings_classification',
    packages=find_packages(include=['kg_plant_seedlings_classification']),
    entry_points={
        'console_scripts': [
            'kg_plant_seedlings_classification=kg_plant_seedlings_classification.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='kg_plant_seedlings_classification',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
