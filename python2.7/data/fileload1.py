#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

integers = pickle.load(open('data/db/file1.dat','rb'))

print(integers)