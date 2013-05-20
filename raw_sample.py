#!/usr/bin/env python

from macropy.macros.adt import macros, case

class Constants:
    missingRawCurrent = 0x7001
    missingRawVoltage = 0xFFFF
    coarseMask = 1
    marker0Mask = 1
    marker1Mask = 2
    markerMask = (marker0Mask | marker1Mask)

@case
class RawSample(mainCurrent, usbCurrent, auxCurrent, voltage):
    """ Wrapper for raw sample collected from Monson power monitor """

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


@case
class Voltage(raw):
    """ Data Converter (raw sample -> voltage) """

    # Voltage is missing from recorded data?
    self.missing = (self.raw == Constants.missingRawVoltage)
    # Recorded data has marker 0 channel?
    self.hasMarker0 = (self.raw & Constants.marker0Mask) != 0
    # Recorded data has marker 1 channel?
    self.hasMarker1 = (self.raw & Constants.marker1Mask) != 0

    def toVolts(self):
        """ Convert voltage to V """
        return (self.raw & (~Constants.markerMask)) * 125.0 / 1e6


@case
class Current(raw):
    """ Data converter (raw sample -> current) """

    # Current is missing from recorded data?
    self.missing = (self.raw == Constants.missingRawCurrent)

    def toMilliAmps(self):
        """ Convert current to mA """
        isCoarse = (self.raw & Constants.coarseMask) != 0
        mA = (self.raw & (~Constants.coarseMask)) / 1000.0
        return (mA * 250.0) if isCoarse else mA
