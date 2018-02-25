#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle

integers = [1,2,3,4,5]
f = open('data/db/file1.dat', 'wb')
pickle.dump(integers, f)
f.close()