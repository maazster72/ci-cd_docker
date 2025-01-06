# Define build argument for architecture
ARG ARCH=amd64
# Use the base image with Jetson Linux and ROS 2 installed based on the architecture
FROM rosbot-base:latest

# Set the environment variable for ROS
ENV ROS_DISTRO=galactic

# Switch to root user for installation
USER root

# Install additional ROS packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-rospkg \
        ros-$ROS_DISTRO-tf2-tools \
        ros-$ROS_DISTRO-tf-transformations \
        ros-$ROS_DISTRO-navigation2 \
        ros-$ROS_DISTRO-nav2-bringup \
        ros-$ROS_DISTRO-nav2-common \
        ros-$ROS_DISTRO-nav2-simple-commander \
        ros-$ROS_DISTRO-gazebo-ros-pkgs \
        ros-$ROS_DISTRO-xacro \
        ros-$ROS_DISTRO-joint-state-publisher \
        ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
        ros-$ROS_DISTRO-ackermann-msgs \
        ros-$ROS_DISTRO-serial-driver \
        ros-$ROS_DISTRO-robot-localization && \
    rm -rf /var/lib/apt/lists/*
    
# MQTT packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        mosquitto \ 
        mosquitto-clients && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install -U \
    paho-mqtt \
    scipy \
    numpy \
    pyserial \
    transforms3d