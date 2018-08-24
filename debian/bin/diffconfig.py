#!/usr/bin/env python3

import optparse
import os.path
import re
import sys

from debian_linux.kconfig import *

def diff(a, b):
    acfg = KconfigFile()
    acfg.read(open(a))
    bcfg = KconfigFile()
    bcfg.read(open(b))
    out = KconfigFile()
    for key, value in bcfg.items():
        if key in acfg and value != acfg[key]:
            out[key] = value
    print(str(out))

if __name__ == '__main__':
    parser = optparse.OptionParser(usage="%prog A B")
    options, args = parser.parse_args()
    diff(args[0], args[1])
