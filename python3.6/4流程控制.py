#/usr/bin/env python
# -*- coding: utf-8 -*-

def ifpass():
  x = int(input('Please enter an integer:'))
  if x< 0:
    x = 0
    print('Negative changed to zero')
  elif x == 0:
    print('Zero')
  elif x == 1:
    print('Single')
  else:
    print('More')


if __name__=='__main__':
  ifpass()