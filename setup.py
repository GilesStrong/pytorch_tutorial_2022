#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open("README.md", encoding="utf-8") as fin:
    long_description = fin.read()

dev_only = ["pre-commit", "black", "flake8", "mypy", "pytest", "pytest-mock", "flaky"]
with open("requirements.txt", encoding="utf-8") as f:
    requirements = [r for r in f.read().strip().split("\n") if r not in dev_only]


exec(open("pkg_name/version.py").read())

setup(
    name="pkg_name",
    version=__version__,  # noqa
    author="My Name",
    author_email="myname@email.com",
    description="Description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/[username]/[name]",
    keywords="deep learning, differential programming, physics, science, statistics",
    packages=find_packages(),
    package_data={"pkg_name": ["py.typed"]},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=requirements,
    # license="GNU Affero General Public License v3.0",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        # "License :: OSI Approved :: GNU Affero General Public License v3.0",
        "Operating System :: MacOS :: MacOS X ",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Development Status :: 1 - Planning",
    ],
)
