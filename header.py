#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

class Header(object):

    def __init__(self, headerSize, identifier, batterySize, captureDate, serial,
            calibrationStatus, voutSetting, voutValue, hardwareRate,
            softwareRate, powerField, currentField, voltageField,
            applicationInfo, samples, sum_):
        self.headerSize = headerSize
        self.identifier = identifier
        self.batterySize = batterySize
        self.captureData = captureDate
        self.serial = serial
        self.softwareRate = softwareRate
        self.powerField = powerField
        self.currentField = currentField
        self.voltageField = voltageField
        self.applicationInfo = applicationInfo
        self.samples = samples
        self.sum_ = sum_

    def getSampleTimestamp(index):
        """ Return timestamp for given sample from its header """
        assert index >= 0

        try:
            sampleLengthMs = 1000.0 / float(hardwareRate)
            delta = datetime.timedelta(milliseconds=int(sampleLengthMs * index))
        except ValueError:
            sys.stderr.write("Could not convert data between formats")
        except:
            sys.stderr.write("Unexpected error: %s" % sys.exc_info()[0])
            raise

        return captureDate + delta


class ApplicationInfo(object):

    def __init__(self, captureSetting, swVersion, runMode, exitCode):
        self.captureSetting = captureSetting
        self.swVersion = swVersion
        self.runMode = runMode
        self.exitCode = exitCode


class Samples(object):

    def __init__(self, captureDataMask, totalCount, statusOffset, statusSize,
            sampleOffset, sampleSize):
        self.captureDataMask = captureDataMask
        self.totalCount = totalCount
        self.statusOffset = statusOffset
        self.statusSize = statusSize
        self.sampleOffset = sampleOffset
        self.sampleSize = sampleSize


class SumValues(object):

    def __init__(self, voltage, current, power):
        self.voltage = voltage
        self.current = current
        self.power = power


class Sum(object):

    def __init__(self, main, usb, aux):
        self.main = main
        self.usb = usb
        self.aux = aux
