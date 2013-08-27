pt4utils
========

Monsoon Power Monitor .pt4 file reader. Reads the binary .pt4 file output from
Monsoon's logger executable and outputs it in CSV format for easier processing
by other tools (Matlab, numpy, etc.)

pt4utils is a heavily based on the Scala script written by Aki Saarinen et al.
for [SmartDiet](https://github.com/akisaarinen/smartdiet).

Usage
-----

    $ python pt4_filereader.py <example.pt4>

License
-------

pt4utils is Copyright (C) 2013, Marcelo Martins.

pt4utils was developed in affiliation with Brown University, Department of
Computer Science. For more information about the department, see
http://www.cs.brown.edu.

pt4utils is distributed under the GNU General Public License v3, which should
be distributed with this program, in file COPYING. The license is also available
at http://www.gnu.org/licenses/gpl-3.0.txt.
