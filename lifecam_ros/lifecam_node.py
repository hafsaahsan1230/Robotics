#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image

def callback(msg):
    rospy.loginfo("Received image: %d x %d" %
                  (msg.width, msg.height))

def main():
    rospy.init_node("lifecam_reader", anonymous=True)

    rospy.Subscriber("/lifecam/image_raw", Image, callback)

    rospy.loginfo("LifeCam HD-3000 node started...")
    rospy.spin()

if __name__ == "__main__":
    main()
