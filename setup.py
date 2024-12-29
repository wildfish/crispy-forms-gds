#!/usr/bin/env python
"""
setup.py

setup() is configured with the project metadata so setup.cfg is used
primarily for options for the various tools used.


"""
import os

from setuptools import setup


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as fp:
        return fp.read()


setup(
    name="crispy-forms-gds",
    version="0.3.2",
    description="Django application to add 'django-crispy-forms' layout objects for the GOV.UK Design System.",
    long_description=read("README.rst"),
    long_description_content_type="text/x-rst",
    author="Wildfish",
    author_email="developers@wildfish.com",
    keywords="Django, django-crispy-forms, gov.uk, design system",
    url="https://github.com/wildfish/crispy-forms-gds",
    packages=[
        "crispy_forms_gds",
        "crispy_forms_gds/layout",
        "crispy_forms_gds/templatetags",
    ],
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    install_requires=[
        "Django>=3.2",
        "django-crispy-forms>=1.9",
    ],
    license="License :: OSI Approved :: BSD License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
