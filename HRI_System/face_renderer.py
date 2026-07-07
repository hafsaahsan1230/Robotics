#!/usr/bin/env python3

import pygame
import rospy

pygame.init()

screen = pygame.display.set_mode((1024,600))

clock = pygame.time.Clock()

rospy.init_node("face_renderer")

while not rospy.is_shutdown():

    screen.fill((0,0,0))

    pygame.draw.circle(screen,(255,255,255),(350,300),100)

    pygame.draw.circle(screen,(255,255,255),(650,300),100)

    pygame.draw.circle(screen,(0,0,0),(350,300),40)

    pygame.draw.circle(screen,(0,0,0),(650,300),40)

    pygame.display.update()

    clock.tick(30)