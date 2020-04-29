#
# Makefile: Commands to simplify the release process
#

# You can set these variable on the command line.
PYTHON = python3.6

# package information
name = $(shell $(PYTHON) setup.py --name)
full = $(shell $(PYTHON) setup.py --fullname)

# Where everything lives
pip := venv/bin/pip3
pytest := venv/bin/pytest
python := venv/bin/python3
django := venv/bin/python3 demo/manage.py
frontend := demo/frontend
nvm := sh ~/.nvm/nvm.sh

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo ""
	@echo "  clean       to clean everything"
	@echo "  venv        to create the virtualenv and install dependencies"
	@echo "  dist        to build the package"
	@echo "  docs        to build the HTML documentation"
	@echo "  tests    	 to run the lint checks and tests"
	@echo "  serve    	 to run the Django demo site"
	@echo

.PHONY: clean-dist
clean-dist:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

.PHONY: clean
clean: clean-dist
	rm -rf venv
	rm -rf .tox
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov
	rm -rf $(frontend)/dist
	rm -rf $(frontend)/node_modules
	rm -f $(frontend)/package-lock.json

venv:
	$(PYTHON) -m venv venv
	$(pip) install --upgrade pip
	$(pip) install --upgrade setuptools
	$(pip) install -r requirements.txt

dist:
	$(python) setup.py sdist bdist_wheel

$(frontend)/node_modules:
	cd $(frontend) && $(nvm) use && npm install

$(frontend)/dist: $(frontend)/node_modules
	cd $(frontend) && $(nvm) use && npm run dev

.PHONY: docs
docs:
	python setup.py build_sphinx

.PHONY: tests
tests:
	PYTHONPATH=src $(pytest)

.PHONY: serve
serve: venv $(frontend)/dist
	PYTHONPATH=src $(django) migrate
	PYTHONPATH=src $(django) runserver

-include *.mk
