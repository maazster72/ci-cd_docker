# Use official ROS 2 Galactic base image
FROM ros:galactic-ros-base-focal

# Set environment variable for ROS
ENV ROS_DISTRO=galactic
    
# Install system packages and dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        gnupg2 \
        lsb-release \
        curl \
        sudo \
        python3-pip \
        build-essential \
        libpcap-dev \
        ros-$ROS_DISTRO-desktop \
        python3-rosdep \
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
        ros-$ROS_DISTRO-robot-localization \
        mosquitto \
        mosquitto-clients \
        micro \
        gedit && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip3 install -U \
    colcon-common-extensions \
    colcon-ros-bundle \
    paho-mqtt \
    scipy \
    numpy \
    pyserial \
    transforms3d

# Set working directory
WORKDIR /workspace

# Copy the local src folder to the workspace
COPY src /workspace/src/

# Build and source the workspace
RUN rosdep update && \
    /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && \
    rosdep install --from-paths src --ignore-src -r -y && \
    colcon build"

# Source setup files for interactive shell
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc && \
    echo "source /workspace/install/setup.bash" >> /root/.bashrc

# Default entrypoint
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash && source /workspace/install/setup.bash && exec bash"]
