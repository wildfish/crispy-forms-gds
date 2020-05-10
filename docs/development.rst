========
Overview
========

This project uses Python 3.6 Django 2.2+, Django Crispy Forms 1.9+ for basic
development. The basic package requirements can be found in ``setup.cfg`` and
everything needed for development is listed in ``requirements.txt``. The demo
site is handy for debugging so you will need to install `nvm`_ to manage node
versions/

.. _nvm: https://github.com/nvm-sh/nvm

Layout
======
The package follows the `recommendations`_ made by Ionel Mărieș and puts the
source code for the package in the ``src`` directory. That does make life
slightly complicated regarding the ``PYTHONPATH`` but that's easily overcome
with the project's makefile.

.. _recommendations: https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure

Makefile
========
The project has a ``Makefile`` that contains a number of targets to make life
easy. You can read a brief description by running ``make`` on the command line::

    make



Demo
====
The project contains a Demo site to show that the various Design System components
work as expected. It's a full Django site so it's good for debugging and generally
mucking around. The ``Makefile`` has targets for building the all the assets::

    make clean-frontend
    make frontend

The target for running the demo site takes care of building all the assets::

    make serve

The demo uses webpack to assemble everything. That gives you two options when
building the assets manually:

1. Build into a single JavaScript file for use running the demo site::

    nvm use
    npm run dev

2. Build into separate JavaScript and CSS files, minified for deployment::

    nvm use
    npm run build

Generally the dev version is sufficient. Ideally you should not rely on this
project for building the assets for production. You might find the webpack
config file handy for getting started with your own version however.


Running tests
=============
You can run the tests for an individual test case, the entire suite or for all
the supported versions of python and Django.

1. Run a specific set of tests, for example::

    PYTHONPATH=src pytest tests/layout/test_accordion


  The ``PYTHONPATH`` needs to be set because of the way the source code is laid out.

2. Run the entire test suite::

    make tests

  This is just the equivalent of ``PYTHONPATH=src pytest``.

3. Run the entire test suite for all versions::

    tox

A summary coverage report will be printed to the console, with an HTML report at
``htmlcov/index.html``.

Development standards
=====================

.. _black: https://github.com/python/black#the-black-code-style
.. _flake8: https://pypi.org/project/flake8/
.. _isort: https://github.com/timothycrosley/isort

This project uses black_, flake8_ and isort_ to enforce consistent python styles. Plugins
for each are added to ``pytest`` to keep you honest. You can also run black and isort on
the command line to reformat your code in one go::

    black src
    isort -rc src

Generally it's better to use editor plugins to make the changes whenever a file is saved.


Documentation
=============

The documentation uses sphinx_ and doc8_. The makefile has handy targets for building
the sphinx docs::

    make clean-docs
    make docs

You can check your penmanship from the command line::

    doc8 docs

.. _sphinx: https://www.sphinx-doc.org/
.. _doc8: https://pypi.org/project/doc8/
