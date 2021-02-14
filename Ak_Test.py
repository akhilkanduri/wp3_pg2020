#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:18:32 2021

@author: lfzt3
"""

import pymsgbox
import matplotlib.pyplot as plt

A = pymsgbox.alert("Launch python working..",title="WP3 Msg")

if A=='OK':
    print('Python File invoked...')
    
# Sample execution
plt.plot(1,2)
plt.show()  