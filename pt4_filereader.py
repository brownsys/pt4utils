#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from header import ApplicationInfo, Header, Samples, Sum, SumValues
from pt4_bitreader import Pt4BitReader
from raw_sample import RawSample
from sample import Sample
from status_packet import Currents, StatusPacket

class UnsupportedHardwareException(Exception): pass

class Pt4FileReader(Pt4BitReader):
    """ Reader for Monsoon Power Monitor .pt4 file """

    def readHeader(self):
        """ Read and return header from Pt4 file
        """
        headerSize = self.readUInt32()
        identifier = self.readString(20)
        batterySize = self.readUInt32()
        captureDate = self.readDateTime()
        serial = self.readString(20)
        calibrationStatus = self.readUInt32()
        voutSetting = self.readUInt32()
        voutValue = self.readFloat32()
        hardwareRate = self.readUInt32()
        softwareRate = self.readFloat32()

        powerField = self.readUInt32()
        currentField = self.readUInt32()
        voltageField = self.readUInt32()

        captureSetting = self.readString(30)
        swVersion = self.readString(10)
        runMode = self.readUInt32()
        exitCode = self.readUInt32()
        totalCount = self.readInt64()

        statusOffset = self.readUInt16()
        statusSize = self.readUInt16()
        sampleOffset = self.readUInt16()
        sampleSize = self.readUInt16()

        initialMainVoltage = self.readUInt16()
        initialUsbVoltage = self.readUInt16()
        initialAuxVoltage = self.readUInt16()

        captureDataMask = self.readUInt16()

        sampleCount = self.readUInt64()
        missingCount = self.readUInt64()

        sumMainVoltage = self.readFloat32()
        sumMainCurrent = self.readFloat32()
        sumMainPower = self.readFloat32()

        sumUsbVoltage = self.readFloat32()
        sumUsbCurrent = self.readFloat32()
        sumUsbPower = self.readFloat32()

        sumAuxVoltage = self.readFloat32()
        sumAuxCurrent = self.readFloat32()
        sumAuxPower = self.readFloat32()

        # Padded to 272 bytes; status packet begins
        self.skipBytes(60)

        appInfo = ApplicationInfo(captureSetting, swVersion, runMode, exitCode)
        samples = Samples(captureDataMask, totalCount, statusOffset, statusSize,
                sampleOffset, sampleSize)

        sumMain = SumValues(sumMainVoltage, sumMainCurrent, sumMainPower)
        sumUsb = SumValues(sumUsbVoltage, sumUsbCurrent, sumUsbPower)
        sumAux = SumValues(sumAuxVoltage, sumAuxCurrent, sumAuxPower)
        sumAll = Sum(sumMain, sumUsb, sumAux)

        return Header(headerSize, identifier, batterySize, captureDate, serial,
                calibrationStatus, voutSetting, voutValue, hardwareRate,
                softwareRate, powerField, currentField, voltageField, appInfo,
                samples, sumAll)

    def readStatusPacket(self):
        """ Read and return status packet from input stream
        """
        length = self.readUInt8()
        packetType = self.readUInt8()
        firmwareVersion = self.readUInt8()
        protocolVersion = self.readUInt8()

        mainFineCurrent = self.readInt16()
        usbFineCurrent = self.readInt16()
        auxFineCurrent = self.readInt16()

        voltage1 = self.readUInt16()

        mainCoarseCurrent = self.readInt16()
        usbCoarseCurrent = self.readInt16()
        auxCoarseCurrent = self.readInt16()

        voltage2 = self.readUInt16()

        outputVoltageSetting = self.readUInt8()
        temperature = self.readUInt8()
        status = self.readUInt8()

        self.skipBytes(3)

        serialNumber = self.readUInt16()
        sampleRate = self.readUInt8()

        self.skipBytes(11)

        initialUsbVoltage = self.readUInt16()
        initialAuxVoltage = self.readUInt16()
        hardwareRevision = self.readUInt8()

        self.skipBytes(11)

        eventCode = self.readUInt8()

        self.skipBytes(2)

        checkSum = self.readUInt8()

        # padded to 1024, sample data begins
        self.skipBytes(692)

        fineCurrent = Currents(mainFineCurrent, usbFineCurrent, auxFineCurrent)
        coarseCurrent = Currents(mainCoarseCurrent, usbCoarseCurrent,
                auxCoarseCurrent)

        # Only suppor hardware revisions from 3+
        # Older revisions have different sample-data format
        if hardwareRevision < 3:
            UnsupportedHardwareException("Old hardware revision ({0}) is not supported due to changes in interpretation of sample data".format(hardwareRevision))

        return StatusPacket(length, packetType, firmwareVersion,
                protocolVersion, fineCurrent, coarseCurrent, voltage1,
                voltage2, outputVoltageSetting, temperature, status,
                serialNumber, sampleRate, initialUsbVoltage, initialAuxVoltage,
                hardwareRevision, eventCode, checkSum)

    def readSample(self, header):
        """ Read and return sample data from input stream
        """
        mainCurrent = usbCurrent = auxCurrent = 0

        if (header.samples.captureDataMask & 0x1000 != 0):
            mainCurrent = self.readInt16()

        if (header.samples.captureDataMask & 0x2000 != 0):
            usbCurrent  = self.readInt16()

        if (header.samples.captureDataMask & 0x4000 != 0):
            auxCurrent = self.readInt16()

        voltage = self.readUInt16()

        return RawSample(mainCurrent, usbCurrent, auxCurrent, voltage)


def readAsVector(filename):
    reader = Pt4FileReader(filename)
    header = reader.readHeader()
    statusPacket = reader.readStatusPacket()
    seq = []

    while reader.isFinished() is False:
        rawSample = reader.readSample(header)
        sample = Sample.fromRaw(rawSample, statusPacket)
        yield (header, statusPacket, sample)

    reader.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {0} <pt4-file>".format(sys.argv[0]))
        sys.exit(1)

    print("# Sample(<Main current (mA)>,<USB Current (mA)>,<Aux Current (mA)>,<Voltage (V)>")
    for smpl in readAsVector(sys.argv[1]):
        print(smpl[2])
