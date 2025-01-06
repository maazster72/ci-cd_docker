#!/usr/bin/env python3
import os
import subprocess
import platform
import sys
import argparse

ROS_SETUP_PATH = "/opt/ros/galactic/setup.bash"
WORKSPACE_SETUP_PATH = "/workspace/install/setup.bash"

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {command}")
        print(e)
        return False

def check_ros_environment():
    print("Checking ROS 2 environment setup...")
    if not os.path.isfile(ROS_SETUP_PATH):
        print(f"Error: ROS setup file not found at {ROS_SETUP_PATH}.")
        return False
    if not os.path.isfile(WORKSPACE_SETUP_PATH):
        print(f"Error: Workspace setup file not found at {WORKSPACE_SETUP_PATH}.")
        return False
    return True

def verify_architecture(expected_arch):
    arch = platform.machine()
    if arch != expected_arch:
        print(f"Warning: Build architecture is {arch}, expected {expected_arch}.")
    else:
        print(f"Architecture check passed: {arch}")
    return arch == expected_arch

def main():
    parser = argparse.ArgumentParser(description="Test ROS 2 build.")
    parser.add_argument("--arch", type=str, default="aarch64", help="Expected architecture (default: aarch64)")
    args = parser.parse_args()

    if not check_ros_environment():
        sys.exit(1)
    
    print("Sourcing ROS 2 and workspace setup files...")
    source_command = f"source {ROS_SETUP_PATH} && source {WORKSPACE_SETUP_PATH}"
    if not run_command(f"/bin/bash -c '{source_command} && ros2 node list'"):
        print("Error: Failed to list ROS 2 nodes. Build might be incorrect.")
        sys.exit(1)
    
    if verify_architecture(args.arch):
        print("Build and architecture tests passed.")
    else:
        print("Warning: Architecture mismatch.")
        sys.exit(1)

if __name__ == "__main__":
    main()

# pipeline
