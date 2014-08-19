#!/usr/bin/python

import OFDMlib.modulate
import sys

OFDMlib.modulate.stream(sys.stdin, sys.stdout, 10000, .01)



