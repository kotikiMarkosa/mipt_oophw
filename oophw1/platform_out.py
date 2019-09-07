import sys
import platform
import os
if 'system.txt' in os.listdir():
    print("WARNING: file system.txt already exists and will be overwritten", file=sys.stderr)
# print(platform.system())
# print(platform.release())

