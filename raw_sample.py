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

class Constants(object):
    missingRawCurrent = 0x7001
    missingRawVoltage = 0xFFFF
    coarseMask = 1
    marker0Mask = 1
    marker1Mask = 2
    markerMask = (marker0Mask | marker1Mask)


class RawSample(object):
    """ Wrapper for raw sample collected from Monson power monitor """

    def __init__(self, mainCurrent, usbCurrent, auxCurrent, voltage):
        self.mainCurrent = mainCurrent
        self.usbCurrent = usbCurrent
        self.auxCurrent = auxCurrent
        self.voltage = voltage

        # Voltage missing from recorded data?
        self.voltageMissing = Voltage(voltage).missing
        # Main current missing from recorded data?
        self.mainCurrentMissing = Current(mainCurrent).missing
        # USB current missing from recorded data?
        self.usbCurrentMissing = Current(usbCurrent).missing
        # Aux current missing from recorded data?
        self.auxCurrentMissing = Current(auxCurrent).missing
        # Any sample fields missing from recorded data?
        self.missing = (self.voltageMissing |
                self.mainCurrentMissing |
                self.usbCurrentMissing  |
                self.auxCurrentMissing)

    def mainCurrentToMilliAmps(self):
        """ Converts main current to mA """
        return Current(mainCurrent).toMilliAmps()


class Voltage(object):
    """ Data Converter (raw sample -> voltage) """

    def __init__(self, raw):
        self.raw = raw
        # Voltage is missing from recorded data?
        self.missing = (self.raw == Constants.missingRawVoltage)
        # Recorded data has marker 0 channel?
        self.hasMarker0 = (self.raw & Constants.marker0Mask) != 0
        # Recorded data has marker 1 channel?
        self.hasMarker1 = (self.raw & Constants.marker1Mask) != 0

    def toVolts(self):
        """ Convert voltage to V """
        return (self.raw & (~Constants.markerMask)) * 125.0 / 1e6


class Current(object):
    """ Data converter (raw sample -> current) """

    def __init__(self, raw):
        self.raw = raw
        # Current is missing from recorded data?
        self.missing = (self.raw == Constants.missingRawCurrent)

    def toMilliAmps(self):
        """ Convert current to mA """
        isCoarse = (self.raw & Constants.coarseMask) != 0
        mA = (self.raw & (~Constants.coarseMask)) / 1000.0
        return (mA * 250.0) if isCoarse else mA
