#!/usr/bin/env python

import csv
import sys

def read_input(file):
    for line in file:
        stripped = line.strip()
        if stripped: yield stripped

def main(): 
    for line in read_input(sys.stdin):
        try:
            for parsed in csv.reader([line], skipinitialspace = True):
                print '|'.join(parsed)
        except csv.Error:
            continue
        
if __name__ == "__main__":
    main()