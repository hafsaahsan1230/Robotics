#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import pygame
import os

class EmotionDisplay:

    def __init__(self):

        rospy.init_node("emotion_display")

        pygame.init()

        self.screen = pygame.display.set_mode(
            (1024, 600),
            pygame.RESIZABLE
        )

        pygame.display.set_caption("")

        self.assets_path = os.path.expanduser(
            "~/catkin_ws/src/HRI_System/assets/emotions"
        )

        self.current_emotion = "neutral"

        rospy.Subscriber(
            "/robot_emotion",
            String,
            self.emotion_callback
        )

    def emotion_callback(self, msg):

        self.current_emotion = msg.data

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

            self.screen.fill((0, 0, 0))

            image_path = os.path.join(
                self.assets_path,
                self.current_emotion + ".jpg"
            )

            if os.path.exists(image_path):

                image = pygame.image.load(image_path)

                width, height = self.screen.get_size()

                image = pygame.transform.scale(
                    image,
                    (width, height)
                )

                self.screen.blit(image, (0, 0))

            pygame.display.flip()

            clock.tick(30)

if __name__ == "__main__":

    EmotionDisplay().run()