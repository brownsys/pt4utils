#!/usr/bin/env python

from macropy.macros.adt import macros, case
import datetime

@case
class Header(headerSize,
        identifier,
        batterySize,
        captureDate,
        serial,
        calibrationStatus,
        voutSetting,
        voutValue,
        hardwareRate,
        softwareRate,
        powerField,
        currentField,
        voltageField,
        applicationInfo,
        samples,
        sum):

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


@case
class ApplicationInfo(captureSetting, swVersion, runMode, exitCode): pass


@case
class Samples(captureDataMask,
        totalCount,
        statusOffset,
        statusSize,
        sampleOffset,
        sampleSize): pass


@case
class SumValues(voltage, current, power): pass


@case
class Sum(main, usb, aux): pass
