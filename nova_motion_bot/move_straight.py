#!/usr/bin/env python3

import rospy
from gazebo_msgs.msg import ModelState
from gazebo_msgs.srv import SetModelState
from gazebo_msgs.srv import GetModelState

def move_model():

    rospy.init_node('move_rover_forward')

    rospy.wait_for_service('/gazebo/get_model_state')
    rospy.wait_for_service('/gazebo/set_model_state')

    get_state = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
    set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)

    rospy.loginfo("Waiting for nova_bot to spawn...")

    # WAIT UNTIL MODEL EXISTS
    while not rospy.is_shutdown():

        try:
            result = get_state('nova_bot', 'world')

            if result.success:
                break

        except:
            pass

        rospy.sleep(0.5)

    rospy.loginfo("nova_bot detected. Starting movement.")
    rospy.loginfo("Waiting 7 seconds before movement...")

    rospy.sleep(7)

    rate = rospy.Rate(30)

    x_position = 0.0

    while not rospy.is_shutdown():

        state_msg = ModelState()

        state_msg.model_name = 'nova_bot'

        state_msg.pose.position.x = x_position
        state_msg.pose.position.y = 0
        state_msg.pose.position.z = 0.18

        # PERFECTLY FLAT ORIENTATION
        state_msg.pose.orientation.x = 0
        state_msg.pose.orientation.y = 0
        state_msg.pose.orientation.z = 0
        state_msg.pose.orientation.w = 1

        state_msg.reference_frame = 'world'

        set_state(state_msg)

        # HUMAN WALKING SPEED
        x_position += 0.0025

        rate.sleep()

if __name__ == '__main__':

    try:
        move_model()

    except rospy.ROSInterruptException:
        pass