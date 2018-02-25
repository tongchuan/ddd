#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import os
d = {}
integers = range(9999)
d['i'] = integers

f = open('data/db/file2.dat','wb')
pickle.dump(d, f) #文件中以 ascii 格式保存数据
f.close()

f = open('data/db/file2-1.dat', 'wb')
pickle.dump(d, f, True) #文件中以二进制格式保存数据

s1 = os.stat('data/db/file2.dat').st_size #得到两个文件的大小
s2 = os.stat('data/db/file2-1.dat').st_size

print('%d, %d, %.2f%%' % (s1, s2, (s2+0.0)/s1*100))