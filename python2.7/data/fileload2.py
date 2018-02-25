#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

f = open('data/db/file2-1.dat', 'rb')
d = pickle.load(f)
f.close()

f = open('data/db/file2.dat', 'rb')
d = pickle.load(f)
f.close()
print d