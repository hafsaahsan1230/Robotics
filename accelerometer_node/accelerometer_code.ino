#include <Wire.h>
#include <ros.h>
#include <std_msgs/Float32MultiArray.h>
#include <MPU6050.h>

// Create MPU6050 object
MPU6050 mpu;

// ROS node handle
ros::NodeHandle nh;

// Float32MultiArray message
std_msgs::Float32MultiArray imu_msg;
ros::Publisher imu_pub("imu_data", &imu_msg);

void setup() {
  // Initialize I2C
  Wire.begin();

  // Initialize ROS node
  nh.initNode();
  nh.advertise(imu_pub);

  // Initialize MPU6050
  mpu.initialize();
  if (!mpu.testConnection()) {
    // Optional: blink LED or Serial print error
  }
}

void loop() {
  int16_t ax, ay, az, gx, gy, gz;

  // Read acceleration and gyro
  mpu.getAcceleration(&ax, &ay, &az);
  mpu.getRotation(&gx, &gy, &gz);

  // Fixed-size array for ROS message
  float imu_data[6];
  imu_data[0] = ax;
  imu_data[1] = ay;
  imu_data[2] = az;
  imu_data[3] = gx;
  imu_data[4] = gy;
  imu_data[5] = gz;

  // Assign data to ROS message
  imu_msg.data_length = 6;  // Important: tell ROS how many values
  imu_msg.data = imu_data;

  // Publish
  imu_pub.publish(&imu_msg);

  nh.spinOnce();
  delay(10);
}
