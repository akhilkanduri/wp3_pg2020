import roslaunch
import rospy
import os
import pymsgbox
import matplotlib.pyplot as plt
import thread

thread.start_new_thread(os.system, ('roslaunch carla_autoware_agent carla_autoware_agent.launch town:=Town03 use_ground_truth_localization:=true use_ground_truth_detection:=true spawn_point:=-74,86,2,0,0,90',))
A = pymsgbox.alert("Launch Frenet Planner ? ",title="WP3 Pkg Invoked")
if A=='OK':
    print('Python File invoked...')
    thread.start_new_thread(os.system, ('python wp3_test/trail_launch.py',))

