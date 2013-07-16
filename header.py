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
