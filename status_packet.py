#!/usr/bin/env python

from macropy.macros.adt import macros, case

@case
class StatusPacket(length,
        packetType,
        firmwareVersion,
        protocolVersion,
        fineCurrent,
        coarseCurrent,
        voltage1,
        voltage2,
        outputVoltageSetting,
        temperature,
        status,
        serialNumber,
        sampleRate,
        initialUsbVoltage,
        initialAuxVoltage,
        hardwareRevision,
        eventCode,
        checkSum): pass


@case
class Currents(main, usb, aux): pass
