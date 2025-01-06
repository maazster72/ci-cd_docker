FROM rosbot-packages:latest

WORKDIR /workspace

# Copy the local src folder
COPY ../src /workspace/src/

# Update rosdep and build
RUN rosdep update && \
    /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && \
    rosdep install --from-paths src --ignore-src -r -y && \
    colcon build"

# Source the workspace
RUN echo "source /workspace/install/setup.bash" >> ~/.bashrc

ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/$ROS_DISTRO/setup.bash && source /workspace/install/setup.bash && exec bash"]
