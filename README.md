# Development of Assistive Robot for Commercial Entity

## Overview

This project presents the development of an assistive robotic platform using a modular architecture based on ROS Noetic. The system was designed to allow independent development, testing, and integration of multiple robotic subsystems including simulation, vision, and sensor modules.

Rather than building a monolithic system, each major component was developed as a standalone package and later integrated within a unified ROS environment. This approach improved scalability, debugging, testing, and future expansion of the robotic platform.

## Modular System Architecture

The project consists of three primary modules:

### 1. Nova Motion Bot (Simulation Module)

The robot platform was designed using Autodesk Fusion 360 and integrated into a ROS Noetic and Gazebo simulation environment.

Features:

* Custom robot model designed in Autodesk Fusion 360
* Gazebo-based simulation
* Corridor navigation environment
* Robot dynamics and motion testing
* Virtual validation before hardware deployment
* ROS-compatible robot description and launch configuration

This module serves as the foundation for testing robotic behavior and integration of additional sensors and subsystems.

---

### 2. LifeCam ROS (Vision Module)

The vision subsystem was developed as an independent ROS package responsible for camera integration and image acquisition.

Features:

* Microsoft LifeCam integration
* Real-time video streaming
* ROS image topic publishing
* Support for computer vision applications
* Image acquisition for future perception and recognition tasks

The module can operate independently or be integrated with the complete robotic system.

---

### 3. Accelerometer / IMU Module

The sensor subsystem was developed separately to acquire motion and orientation-related information from the robot.

Features:

* Accelerometer and IMU data acquisition
* Arduino-based sensor interfacing
* ROS topic publishing
* Real-time motion monitoring
* Sensor data integration with ROS nodes

The modular design allows the sensor package to be tested independently before integration with the complete robotic platform.

---

## Integration Strategy

After independent development and validation of each subsystem, the modules were integrated within a ROS Noetic Catkin workspace.

Integrated capabilities include:

* Robot simulation in Gazebo
* Camera data acquisition
* Motion and sensor monitoring
* ROS-based communication between nodes
* Scalable architecture for future development

The modular approach significantly reduced development complexity and enabled individual testing of components before full-system deployment.

## Technologies Used

* ROS Noetic
* Gazebo
* Autodesk Fusion 360
* Ubuntu Linux
* Python
* C++
* Arduino
* Catkin Workspace

## Project Structure

```text
Assistive Robot System
│
├── Nova Motion Bot
│   └── Gazebo Simulation Module
│
├── LifeCam ROS
│   └── Vision Module
│
├── Accelerometer / IMU Module
│   └── Sensor Module
│
└── Integrated ROS Catkin Workspace
    └── Combined System
```

## Engineering Approach

The project follows a modular robotics design philosophy where simulation, perception, and sensing components are developed as independent packages. This architecture promotes maintainability, reusability, easier debugging, and future expansion of the robotic platform.

## Future Enhancements

* Autonomous navigation
* Obstacle avoidance
* Computer vision and object recognition
* SLAM integration
* Voice interaction
* Remote monitoring and control
* Deployment on physical robotic hardware
