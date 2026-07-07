#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import pygame
import os

class AdvertisementDisplay:

    def __init__(self):

        rospy.init_node("advertisement_display")

        pygame.init()

        self.screen = pygame.display.set_mode(
            (500, 700),
            pygame.RESIZABLE
        )

        pygame.display.set_caption(
            ""
        )

        self.current_ad = "ad1"

        self.ads_path = os.path.expanduser(
            "~/catkin_ws/src/HRI_System/assets/ads"
        )

        rospy.Subscriber(
            "/robot_ad",
            String,
            self.ad_callback
        )

    def ad_callback(self, msg):

        self.current_ad = msg.data

    def run(self):

        clock = pygame.time.Clock()

        while not rospy.is_shutdown():

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    return

                elif event.type == pygame.VIDEORESIZE:

                    self.screen = pygame.display.set_mode(
                        (event.w, event.h),
                        pygame.RESIZABLE
                    )

            self.screen.fill((255,255,255))

            image_path = os.path.join(
                self.ads_path,
                self.current_ad + ".jpg"
            )

            if os.path.exists(image_path):

                image = pygame.image.load(image_path)

                width, height = self.screen.get_size()

                image = pygame.transform.scale(
                    image,
                    (width, height)
                )

                self.screen.blit(image,(0,0))

            pygame.display.flip()

            clock.tick(30)

if __name__ == "__main__":

    AdvertisementDisplay().run()