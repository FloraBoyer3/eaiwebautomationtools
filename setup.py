# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name="eaiautomatontools",
    version="1.1.8",
    description="UI utilities in order to abstract selenium commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://eaiwebautomationtools.readthedocs.io/",
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # 'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'selenium>=4.0',
        'Pillow>=8.1.1',
        'webdriver-manager',
        'Deprecated',
        'polling2'
    ],
    python_requires='>=3.7, !=2.*',
    packages=find_packages(),
    include_package_data=True,
    # package_dir={'': 'eaiautomatontools'},
    author="Eric Aïvayan",
    author_email="eric.aivayan@free.fr"
)
