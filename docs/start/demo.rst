.. _crispy-forms-gds: https://github.com/wildfish/crispy-forms-gds
.. _makefile: https://github.com/wildfish/crispy-forms-gds/blob/master/Makefile

=========
Demo Site
=========
If you checked out or downloaded the source for `crispy-forms-gds`_ from the
repository then you can run the Django demo site to see all Design System
components in action.

The project has a `makefile`_ in the project root that simplifies setting everything
up. To run the Django demo site simply type: ::

    make serve

The makefile installs all the dependencies including the javascript that contains the
Design System and and builds everything needed to run the Django site. Now you can
just point your browser at ``http://localhost:8000/`` to see example forms for each
supported component.
