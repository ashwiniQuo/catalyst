import os
import subprocess
import json
from setuptools import setup, find_packages

VERSION = "1.0"

setup(
    name='catalyst',
    description=("An aritifical intelligent bot"),
    version=VERSION,
    packages=["catalyst"],
    include_package_data=True,
    zip_safe=False,
    scripts=['catalyst/bin/catalyst'],
    install_requires=[],
    author='Abhishek Shukla',
    author_email='shuklaabhishek02@gmail.com',
    url='https://github.com/shuklaabhi/catalyst',
    download_url=('https://github.com/shuklaabhi/catalyst/tarball/' + VERSION),
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)