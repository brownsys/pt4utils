#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
