# Sujet_4__Bob_le_nettoyeur

This project allows to control a robot from an Android application.
This robot is able to move in a space while he is cleaning a table.

There is two modes:
- "control" mode = manual mode
- "auto" mode = automatic mode

A little sensor is allowing to detect the end of the table to not fall out of the table.


## User Manual

First you need to be sure to have ROS kinetic installed and "dynamixel_motor" git repo must be installed.


```bash
roscore
```

```bash
roslaunch detection control_all_launch.launch
```