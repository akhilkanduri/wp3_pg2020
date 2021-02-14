#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:49:25 2021

@author: lfzt3
"""

import roslaunch
import rospy
import os
import pymsgbox
import matplotlib.pyplot as plt

A = pymsgbox.alert("Launch Frenet Planner ? ",title="WP3 Pkg Invoked")

if A=='OK':
    print('Python File invoked...')
    os.system("roslaunch carla_autoware_agent carla_autoware_agent.launch town:=Town03 use_ground_truth_localization:=true use_ground_truth_detection:=true spawn_point:=-74,86,2,0,0,90 & python Ak_Test.py &")    
