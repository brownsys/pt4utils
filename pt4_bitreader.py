#!/usr/bin/env python

from datetime import datetime
from bitreader import BitReader

class Pt4BitReader(BitReader):
    """ Interpreter for binary stream from Pt4 file """

    def readDateTime(self):
        """ Read and return date in epoch format
        """
        epochShiftValue = 62135596800000L
        val = self.readUInt64()
        kind = val >> 62
        ticks = val & 0x3FFFFFFFFFFFFFFFL
        #return datetime.fromtimestamp((ticks / 10000) - epochShiftValue)
        return 0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
