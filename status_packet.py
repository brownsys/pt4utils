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

class StatusPacket(object):

    def __init__(self, length, packetType, firmwareVersion, protocolVersion,
        fineCurrent, coarseCurrent, voltage1, voltage2, outputVoltageSetting,
        temperature, status, serialNumber, sampleRate, initialUsbVoltage,
        initialAuxVoltage, hardwareRevision, eventCode, checkSum):
        self.length = length
        self.packetType = packetType
        self.firmwareVersion = firmwareVersion
        self.protocolVersion = protocolVersion
        self.fineCurrent = fineCurrent
        self.coarseCurrent = coarseCurrent
        self.voltage1 = voltage1
        self.voltage2 = voltage2
        self.outputVoltageSetting = outputVoltageSetting
        self.temperature = temperature
        self.status = status
        self.serialNumber = serialNumber
        self.sampleRate = sampleRate
        self.initialUsbVoltage = initialUsbVoltage
        self.initialAuxVoltage = initialAuxVoltage
        self.hardwareRevision = hardwareRevision
        self.eventCode = eventCode
        self.checkSum = checkSum


class Currents(object):

    def __init__(self, main, usb, aux):
        self.main = main
        self.usb = usb
        self.aux = aux
