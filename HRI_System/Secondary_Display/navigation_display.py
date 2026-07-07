#!/usr/bin/env python3

import rospy
import pygame
import os
import math

class NavigationDisplay:

    def __init__(self):

        rospy.init_node("navigation_display")

        pygame.init()

        self.screen = pygame.display.set_mode(
            (1400,900),
            pygame.RESIZABLE
        )

        pygame.display.set_caption(
            ""
        )

        self.map_path = os.path.expanduser(
            "~/catkin_ws/src/HRI_System/assets/maps/corridor_map.jpg"
        )

        self.map_image = pygame.image.load(
            self.map_path
        )

        self.path_points = [

            (250,850),
            (250,700),
            (250,550),
            (250,400),
            (250,250),

            (450,250),
            (650,250),
            (850,250),

            (1050,250),
            (1250,250),
            (1450,250)

        ]

        self.current_target = 1

        self.robot_x = self.path_points[0][0]
        self.robot_y = self.path_points[0][1]

        self.clock = pygame.time.Clock()

    def update_robot(self):

        target = self.path_points[
            self.current_target
        ]

        dx = target[0] - self.robot_x
        dy = target[1] - self.robot_y

        dist = math.sqrt(
            dx * dx + dy * dy
        )

        speed = 2

        if dist < speed:

            self.robot_x = target[0]
            self.robot_y = target[1]

            self.current_target += 1

            if self.current_target >= len(
                self.path_points
            ):

                self.current_target = 0

        else:

            self.robot_x += (
                speed * dx / dist
            )

            self.robot_y += (
                speed * dy / dist
            )

    def run(self):

        title_font = pygame.font.SysFont(
            None,
            60
        )

        while not rospy.is_shutdown():

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    return

                elif event.type == pygame.VIDEORESIZE:

                    self.screen = pygame.display.set_mode(
                        (event.w,event.h),
                        pygame.RESIZABLE
                    )

            self.screen.fill(
                (255,255,255)
            )

            width, height = self.screen.get_size()

            map_surface = pygame.transform.scale(
                self.map_image,
                (width - 100,
                 height - 150)
            )

            self.screen.blit(
                map_surface,
                (50,80)
            )

            self.update_robot()

            pygame.draw.circle(
                self.screen,
                (255,0,0),
                (
                    int(self.robot_x),
                    int(self.robot_y)
                ),
                15
            )

            pygame.draw.circle(
                self.screen,
                (255,100,100),
                (
                    int(self.robot_x),
                    int(self.robot_y)
                ),
                30,
                3
            )

            title = title_font.render(
                "",
                True,
                (0,0,255)
            )

            self.screen.blit(
                title,
                (500,20)
            )

            pygame.display.flip()

            self.clock.tick(60)

if __name__ == "__main__":

    NavigationDisplay().run()
