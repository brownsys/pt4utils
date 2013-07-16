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

import os
import struct
import sys

class BitReader(object):
    """ Interpreter for binary stream """

    def __init__(self, filename):
        try:
            self.filesize = os.stat(filename).st_size
            self.fin = (open(filename, "rb"))
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

    def close(self):
        """ Close binary stream """
        try:
            self.fin.close()
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

    def skipBytes(self, nbytes):
        """ Forward and ignore nbytes from current reading position
        """
        try:
            self.fin.seek(nbytes, os.SEEK_CUR)
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

    def readUInt8(self):
        """ Read and return unsigned 8-bit integer from input
        """
        try:
            # B = unsigned char
            val = struct.unpack('B', self.fin.read(1))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readInt8(self):
        """ Read and return signed 8-bit integer from input
        """
        try:
            # b = signed char
            val = struct.unpack('b', self.fin.read(1))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readFloat32(self):
        """ Read and return 32-bit floating-point number from input
        """
        try:
            # f = floating point (4 bytes)
            val = struct.unpack('f', self.fin.read(4))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readUInt16(self):
        """ Read and return unsigned 16-bit integer from input
        """
        try:
            # H = unsigned short (2 bytes)
            val = struct.unpack('H', self.fin.read(2))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readInt16(self):
        """ Read and return signed 16-bit integer from input
        """
        try:
            # h = short (2 bytes)
            val = struct.unpack('h', self.fin.read(2))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readUInt32(self):
        """ Read and return unsigned 32-bit integer from input
        """
        try:
            # I = unsigned int (4 bytes)
            val = struct.unpack('I', self.fin.read(4))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readInt32(self):
        """ Read and return signed 32-bit integer from input
        """
        try:
            # i = int (4 bytes)
            val = struct.unpack('i', self.fin.read(4))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readUInt64(self):
        """ Read and return unsigned 64-bit integer from input
        """
        try:
            # Q = unsigned long long (8 bytes)
            val = struct.unpack('Q', self.fin.read(8))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readInt64(self):
        """ Read and return signed 64-bit integer from input
        """
        try:
            # q = long long (8 bytes)
            val = struct.unpack('q', self.fin.read(8))[0]
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return val

    def readString(self, length):
        """ Read and return length-byte string from input
        """
        assert length >= 0

        try:
            s = self.fin.read(length)
            return s.strip()
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()
        except:
            sys.stderr.write("Unexpected error: %s\n" % sys.exc_info()[0])
            raise

        return None

    def isFinished(self):
        """ Return whether finished to read input
        """
        try:
            return self.fin.tell() == self.filesize
        except IOError, (errno, strerror):
            sys.stderr.write("I/O error(%s): %s\n" % (errno, strerror))
            self.fin.close()

        return True
