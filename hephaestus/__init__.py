# -*- coding: utf-8 -*-
from pkg_resources import get_distribution, DistributionNotFound
import os

from simple_settings import settings


# TODO: Remove the next line before pushing module
# settings below indicates settings.py file
# This can be provided on the commandline: Ref: https://pypi.org/project/simple-settings/
os.environ.setdefault('SIMPLE_SETTINGS', 'settings')

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = 'hephaestus'
    __version__ = get_distribution(dist_name).version
except DistributionNotFound:
    __version__ = 'unknown'
