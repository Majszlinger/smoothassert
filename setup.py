# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pandas>=0.24","numpy>=1.17","scikit-learn>=0.21"]

setup(
    name="smoothassert",
    version="0.1.2",
    author="Tamás Majszlinger",
    author_email="tomcsojn@gmail.com",
    description="Custom Assertions for unittest with Pandas.Series and DataFrames. Similarity tests, based on pandas.testing",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Majszlinger/smoothassert",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)