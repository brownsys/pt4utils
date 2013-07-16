#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
