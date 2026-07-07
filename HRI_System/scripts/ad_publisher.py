#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node("ad_publisher")

pub = rospy.Publisher(
    "/robot_ad",
    String,
    queue_size=10
)

ads = [

    "ad1",

    "ad2",

    "ad3"
]

rate = rospy.Rate(0.05)

i = 0

while not rospy.is_shutdown():

    pub.publish(ads[i])

    i = (i + 1) % len(ads)

    rate.sleep()
