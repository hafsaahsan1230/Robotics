#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node("location_publisher")

pub = rospy.Publisher(
    "/robot_location",
    String,
    queue_size=10
)

locations = [

    "Reception",

    "Lab A",

    "Library",

    "Seminar Hall",

    "Dean Office"
]

rate = rospy.Rate(0.1)

i = 0

while not rospy.is_shutdown():

    pub.publish(locations[i])

    i = (i + 1) % len(locations)

    rate.sleep()