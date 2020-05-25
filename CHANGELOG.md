# Change Log
All notable changes to this project will be documented in this file.
Only changes for the API functions are described here. Changes made 
to the internals and developing the package are not included. Check 
the git log for details.

The format is based on [Keep a Changelog](http://keepachangelog.com/).
This project adheres to [PEP440](https://www.python.org/dev/peps/pep-0440/)
and by implication, [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Changed
- Simplified webpack configuration for demo site.
- Synchronized demo site and package licences and versions.

## [0.2.0] - 2020-05-16
### Added 
- Hints can now be added to checkboxes and radios.
- Accordion sections can now display a summary of the contents.
- Merged the templatetags so all you have to do is {% load crispy_forms_gds %}.
- Added the fields and templates needed for the Date input component.
- Added template tags for back links, start buttons and breadcrumbs.
- Added a production-ready base template that can be used in sites.
- Added a Choice class to make setting hints and dividers on checkboxes 
  and radio buttons cleaner and easier.
### Changed
- Updated Table component to support a caption and CSS styling.
### Deleted
- Removed the hints attribute on Field.checkboxes() and Field.radios()

## [0.1.0] - 2020-04-28
### Added
- Added all the form-level components from the Design System. The only
  one missing is Date input.

## [0.0.1] - 2020-04-03
### Added 
- All the project files needed to generate the package documentation.
- All the project files needed to release the package to PyPI.
- Set of core templates for rendering forms.
- Layout object for rendering submit buttons.
- Tests for verifying text inputs are rendered correctly.
- Django site for showing how the forms are used. 
