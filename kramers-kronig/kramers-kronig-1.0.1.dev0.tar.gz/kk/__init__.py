"""Functions to compute Kramers-Kronig relations."""

from pkg_resources import get_distribution

from kk.fft import *


__version__ = get_distribution("kramers-kronig").version

__title__ = "Kramers-Kronig"
__description__ = "Kramers-Kronig relations."
__uri__ = "https://gitlab.com/fblanchet/kramers-kronig"

__author__ = "Florian Blanchet"
__email__ = "florian.blanchet@supoptique.org"
__license__ = "Apache Software License"
__copyright__ = "2020 Florian Blanchet"

__all__ = ["__version__"]
