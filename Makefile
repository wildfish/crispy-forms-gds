#
# Makefile: Commands to simplify the release process
#
# Generally the targets are generally idempotent and reversible. For
# every target that does something, there is a corresponding clean
# target that undoes it. The obvious exception is uploading a package
# to PyPI which cannot be undone.
#
# Also the targets avoid making changes that are harder to undo. For
# example git changes generally need quite a bit of checking before the
# command can proceed, e.g. checking for uncommitted changes before adding
# a tag. The additional steps make using the command more brittle and so
# are generally avoided. A good process will be more reliable than a
# high-level of automation. Having said that we will add targets whenever
# it makes life easier.


# You can set these variable on the command line.
# Only set VERSION when running 'make version`
PYTHON = python3.6
VERSION =

# Where everything lives
pip := venv/bin/pip3
pytest := venv/bin/pytest
python := venv/bin/python3
twine := venv/bin/twine
django := venv/bin/python3 demo/manage.py
frontend := demo/frontend
nvm := sh ~/.nvm/nvm.sh

# files that are updated by the 'version' target.
config_file := setup.cfg
version_file := src/crispy_forms_gds/__init__.py
changelog_file = CHANGELOG.md
docs_file := docs/conf.py
package_file := demo/frontend/package.json

version_files := $(config_file) $(version_file) $(changelog_file) $(docs_file) $(package_file)

docs_version := $(shell echo $(VERSION) | cut -d '.' -f 1,2)
docs_release := $(VERSION)

# All releases must be signed.
# https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
gpg_key_id := `git config --global --get user.signingkey`
upload_opts := --sign --identity $(gpg_key_id)
test_upload_opts := --repository testpypi $(upload_opts)


.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo ""
	@echo "  clean           to clean everything"
	@echo "  clean-dist      to clean the files and directories created by the dist target"
	@echo "  clean-docs      to clean the generated HTML documentation"
	@echo "  clean-frontend  to clean the frontend assets and node packages"
	@echo "  clean-tests     to clean the directories created when running tox or pytest"
	@echo "  clean-venv      to clean the virtualenv"
	@echo "  clean-version   to revert the changes to files containing the version number"
	@echo
	@echo "  dist            to build the package"
	@echo "  docs            to build the HTML documentation"
	@echo "  frontend        to install and build the Design System assets for the demo site"
	@echo "  help            to show this list"
	@echo "  serve           to run the Django demo site"
	@echo "  tests           to run the tests using pytest during development"
	@echo "  test-upload     to upload a signed release to the PyPI test repository"
	@echo "  upload          to upload a signed release to PyPI repository"
	@echo "  venv            to create the virtualenv and install dependencies"
	@echo "  version         to update the files containing the package version number"
	@echo "                     you must set the VERSION on the command line, for example"
	@echo "                     make version VERSION=1.2.3"
	@echo

.PHONY: clean-dist
clean-dist:
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info

.PHONY: clean-docs
clean-docs:
	cd docs && make clean && cd ..

.PHONY: clean-frontend
clean-frontend:
	rm -rf $(frontend)/dist
	rm -rf $(frontend)/node_modules
	rm -f $(frontend)/package-lock.json

.PHONY: clean-tests
clean-tests:
	rm -rf .tox
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf htmlcov

.PHONY: clean-venv
clean-venv:
	rm -rf venv

.PHONY: clean-version
clean-version:
	git restore --staged $(version_files)
	git restore $(version_files)

.PHONY: clean
clean: clean-dist clean-docs clean-frontend clean-tests clean-venv clean-version

dist:
	$(python) setup.py sdist bdist_wheel
	$(twine) check dist/*

.PHONY: docs
docs:
	python setup.py build_sphinx

$(frontend)/node_modules:
	cd $(frontend) && $(nvm) use && npm install

$(frontend)/dist: $(frontend)/node_modules
	cd $(frontend) && $(nvm) use && npm run dev

.PHONY: frontend
frontend: $(frontend)/dist

.PHONY: serve
serve: venv frontend
	PYTHONPATH=src $(django) migrate
	PYTHONPATH=src $(django) runserver

.PHONY: tests
tests:
	PYTHONPATH=src $(pytest)

.PHONY: test-upload
test-upload: dist
	$(twine) upload $(test_upload_opts) dist/*

.PHONY: upload
upload: dist
	$(twine) upload $(upload_opts) dist/*

venv:
	$(PYTHON) -m venv venv
	$(pip) install --upgrade pip
	$(pip) install --upgrade setuptools
	$(pip) install -r requirements.txt

.PHONY: version
version:
	[ -n "$(VERSION)" ]
	sed -i "s/^version = .*/version = \"$(docs_version)\"/" $(docs_file)
	sed -i "s/^release = .*/release = \"$(docs_release)\"/" $(docs_file)
	git add $(docs_file)
	sed -i "s/^version = .*/version = $(VERSION)/" $(config_file)
	git add $(config_file)
	sed -i "s/^__version__ = .*/__version__ = \"$(VERSION)\"/" $(version_file)
	git add $(version_file)
	sed -i "s/^  \"version\": .*/  \"version\": \"$(VERSION)\",/" $(package_file)
	git add $(package_file)
	awk -i inplace -v version=$(VERSION) -v date=`date +%Y-%m-%d` \
		'NR==1,/^##.*/{sub(/^##.*/, "## ["version"] - "date)} 1' $(changelog_file)
	git add $(changelog_file)

# include any local makefiles
-include *.mk
