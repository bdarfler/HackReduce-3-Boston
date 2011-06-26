#!/usr/bin/env python

import sys 
from itertools import groupby
from operator import itemgetter

def read_input(file):
    for line in file:
        stripped = line.strip()
        if stripped: yield line.split('\t', 2)

def main():        
    for fingerprint, fgroup in groupby(read_input(sys.stdin), itemgetter(1)):
        names = []
        for name, ngroup in groupby(fgroup, itemgetter(2)):            
            names.append(name.strip())
        if len(names) > 1:    
            print '%s\t%s' % (fingerprint.strip(), names)  
                        

if __name__ == "__main__":
    main()