"""This module contains WFC3/IR commissioning tests.
Adapted from ``astrolib/pysynphot/from_commissioning/wfc3_ir/test3.py``.
"""
from __future__ import absolute_import, division, print_function

# LOCAL
from ..utils import ThermCase


class Test1361(ThermCase):
    # Original test used gal1 but it is no longer supported, so we use gal3
    obsmode = 'wfc3,ir,f160w'
    spectrum = ('rn(spec($PYSYN_CDBS/grid/pickles/dat_uvk/pickles_uk_100.fits)'
                ',band(cousins,i),28.0,vegamag)*ebmvx(0.04,gal3)')
