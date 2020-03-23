#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ERPNextClient", # Replace with your own username
    version="0.1",
    author="Guillaume Libersat",
    author_email="glibersat@singe-savant.com",
    description="ERPNext REST API Client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/singesavant/erpnext-rest-client",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5'
)
