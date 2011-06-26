#!/usr/bin/env python

import csv
import re
import string
import sys
import unicodedata

def remove_accents(str):
    nkfd_form = unicodedata.normalize('NFKD', unicode(str,'utf8','ignore'))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])

def read_input(file):
    for line in file:
        stripped = line.strip()
        if stripped: yield stripped

def main():
    alphanum = re.compile('[\x00-\x1F\x7F%s]' % re.escape(string.punctuation))

    for line in read_input(sys.stdin):
        try: 
            for parsed in csv.reader([line], skipinitialspace = True):
                name = parsed[1]
                cleaned = re.sub(alphanum, '', name.strip().lower())
                deduped = ' '.join(sorted(set(cleaned.split())))
                key = remove_accents(deduped).encode('utf8')
                print '%s:%s\t%s\t%s' % (key, name, key, name)
        except csv.Error:
            continue
        
if __name__ == "__main__":
    main()