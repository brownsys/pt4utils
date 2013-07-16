#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This file is part of pt4utils.
#
# Copyright (C) 2013, Marcelo Martins.
#
# pt4utils was developed in affiliation with Brown University,
# Department of Computer Science. For more information about the
# department, see <http://www.cs.brown.edu/>.
#
# pt4utils is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pt4utils is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pt4utils.  If not, see <http://www.gnu.org/licenses/>.
#

from datetime import datetime
from bitreader import BitReader

class Pt4BitReader(BitReader):
    """ Interpreter for binary stream from Pt4 file """

    def readDateTime(self):
        """ Read and return date in epoch format
        """
        epochShiftValue = 62135596800000L
        val = self.readUInt64()
        kind = val >> 62
        ticks = val & 0x3FFFFFFFFFFFFFFFL
        #return datetime.fromtimestamp((ticks / 10000) - epochShiftValue)
        return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
