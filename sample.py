#!/usr/bin/env python

from macropy.macros.adt import macros, case
from raw_sample import Current, RawSample, Voltage

@case
class Sample(mainCurrent, usbCurrent, auxCurrent, voltage):
    """ Wrapper for sample from Monsoon power monitor """
    pass


def fromRaw(rawSample, statusPacket):
    """ Create and return sample from raw data """
    mainCurrent = Current(rawSample.mainCurrent)
    usbCurrent = Current(rawSample.usbCurrent)
    auxCurrent = Current(rawSample.auxCurrent)
    voltage = Voltage(rawSample.voltage)

    return Sample(mainCurrent.toMilliAmps(), usbCurrent.toMilliAmps(),
            auxCurrent.toMilliAmps(), voltage.toVolts())
