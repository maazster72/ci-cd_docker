# Use official ROS 2 Galactic base image from Docker Hub
FROM ros:galactic-ros-base-focal

# Set environment variables to avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    lsb-release \
    gnupg2 \
    curl \
    wget \
    ca-certificates \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for ROS 2
ENV ROS_DISTRO=galactic
ENV ROS_SETUP="/opt/ros/galactic/setup.bash"

# Source ROS 2 setup script to configure the environment
RUN echo "source $ROS_SETUP" >> /root/.bashrc

# Default entrypoint: start a shell
CMD [ "bash" ]
