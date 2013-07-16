#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
