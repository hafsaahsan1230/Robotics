#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node("emotion_publisher")

pub = rospy.Publisher(
    "/robot_emotion",
    String,
    queue_size=10
)

rate = rospy.Rate(0.2)

emotions = [
    "happy",
    "excited",
    "sad"
]

i = 0

while not rospy.is_shutdown():

    pub.publish(emotions[i])

    i = (i + 1) % len(emotions)

    rate.sleep()