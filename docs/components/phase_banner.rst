.. _Phase banner: https://design-system.service.gov.uk/components/phase-banner/

############
Phase banner
############
There is a `Phase banner`_ component implemented in the ``gds/base.html`` template
that is include in the template pack. It is wrapped with a ``{% block %}`` tag so if
you extend the base template you can override it if you need to.

Within the ``{% block phase_banner %}`` tag there are two daughter blocks:
``{% block phase_banner__tag %}`` and ``{% block phase_banner__text %}`` so you can
selectively override these if you don't want to override the entire phase_banner
block.
