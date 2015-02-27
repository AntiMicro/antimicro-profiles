#!/usr/bin/env python

import os
import sys

def usage():
    print("Usage: python util.py <appname>")
    print("")
    print("""Used to create a skeleton directory structure for storing profiles.""")
    print("")
    print("-h, --help          Print help text")

def main():
    appname = sys.argv[1]
    appdir = os.path.realpath(os.path.dirname(appname))
    if not os.path.isdir(appdir):
        appdir = os.getcwd()

    appname = appname.replace(":", " - ")
    folder_path = [appdir, "applications", appname, "sdlgamecontroller"]
    final_path = os.path.realpath(os.path.join(*folder_path))
    os.makedirs(final_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)
    elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
        usage()
        sys.exit(0)
    else:
        main()

