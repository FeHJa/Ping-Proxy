#!/usr/bin/env python
import sys
import os

def pname_exists(inp):
    os.system('ps -ef > /tmp/psef')
    lines=open('/tmp/psef', 'r').read().split('\n')
    res=[i for i in lines if inp in i]
    return True if res else False

if pname_exists("script.py"):
	sys.exit(0)
else:
	sys.exit(1)