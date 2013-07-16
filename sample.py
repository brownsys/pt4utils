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

from raw_sample import Current, RawSample, Voltage

class Sample(object):
    """ Wrapper for sample from Monsoon power monitor """

    def __init__(self, mainCurrent, usbCurrent, auxCurrent, voltage):
        self.mainCurrent = mainCurrent
        self.usbCurrent = usbCurrent
        self.auxCurrent = auxCurrent
        self.voltage = voltage

    def __str__(self):
        return "{0},{1},{2},{3}".format(self.mainCurrent, self.usbCurrent,
                self.auxCurrent, self.voltage)

    @staticmethod
    def fromRaw(rawSample, statusPacket):
        """ Create and return sample from raw data """
        mainCurrent = Current(rawSample.mainCurrent)
        usbCurrent = Current(rawSample.usbCurrent)
        auxCurrent = Current(rawSample.auxCurrent)
        voltage = Voltage(rawSample.voltage)

        return Sample(mainCurrent.toMilliAmps(), usbCurrent.toMilliAmps(),
                auxCurrent.toMilliAmps(), voltage.toVolts())
