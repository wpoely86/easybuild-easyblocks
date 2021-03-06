##
# Copyright 2013 Ghent University
#
# This file is part of EasyBuild,
# originally created by the HPC team of Ghent University (http://ugent.be/hpc/en),
# with support of Ghent University (http://ugent.be/hpc),
# the Flemish Supercomputer Centre (VSC) (https://vscentrum.be/nl/en),
# Flemish Research Foundation (FWO) (http://www.fwo.be/en)
# and the Department of Economy, Science and Innovation (EWI) (http://www.ewi-vlaanderen.be/en).
#
# http://github.com/hpcugent/easybuild
#
# EasyBuild is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation v2.
#
# EasyBuild is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EasyBuild.  If not, see <http://www.gnu.org/licenses/>.
##
"""
EasyBuild support for building and installing a Pythonpackage independend of a python version as an easyblock.

This easyblock is no longer supported, and is replaced by VersionIndependentPythonPackage (fixes a typo in the class name).

@author: Kenneth Hoste, Jens Timmerman (Ghent University)
"""
from easybuild.easyblocks.generic.versionindependentpythonpackage import VersionIndependentPythonPackage


class VersionIndependendPythonPackage(VersionIndependentPythonPackage):
    """No longer supported class for building/installing python packages without requiring a specific python package."""

    def prepare_step(self):
        """Indicate that this easyblock is no longer supported."""
        self.log.nosupport("Replaced by VersionIndependentPythonPackage easyblock", '2.0')
