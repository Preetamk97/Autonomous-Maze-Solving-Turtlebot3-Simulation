#! /usr/bin/env python3

# This node sets the initial starting position of our Turtlebot in the RViz2 map and also sets the goal point that the robot has to reach in the RViz2 map - and sets our robot in motion.

# Base code copied from the Official Github Account of ROS Planning :  ros-planning/navigation2 ('humble' branch)/nav2_simple_commander/nav2_simple_commander/example_nav_to_pose.py
# Modified as per the current project needs.

from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator, TaskResult
import rclpy
from rclpy.duration import Duration


def main():
    rclpy.init()

    navigator = BasicNavigator()

    # Setting the Initial Starting Position of our Robot
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = navigator.get_clock().now().to_msg()
    initial_pose.pose.position.x = -3.915259599685669
    initial_pose.pose.position.y = -7.872808456420898
    initial_pose.pose.orientation.z = 0.2
    initial_pose.pose.orientation.w = 0.9999933969549617
    navigator.setInitialPose(initial_pose)

    # Wait for navigation to fully activate
    navigator.waitUntilNav2Active()

    # Setting the Final Goal Position of our Robot
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = 8.194306373596191
    goal_pose.pose.position.y = 0.2381921410560608
    goal_pose.pose.orientation.z = 0.2
    goal_pose.pose.orientation.w = 0.9999549894419945
    navigator.goToPose(goal_pose)

    i = 0
    while not navigator.isTaskComplete():
        # Do something with the feedback
        i = i + 1
        feedback = navigator.getFeedback()
        if feedback and i % 5 == 0:
            print('Estimated time of arrival: ' + '{0:.0f}'.format(
                  Duration.from_msg(feedback.estimated_time_remaining).nanoseconds / 1e9)
                  + ' seconds.')

    # Do something depending on the return code
    result = navigator.getResult()
    if result == TaskResult.SUCCEEDED:
        print('Goal succeeded!')
    elif result == TaskResult.CANCELED:
        print('Goal was canceled!')
    elif result == TaskResult.FAILED:
        print('Goal failed!')
    else:
        print('Goal has an invalid return status!')

    navigator.lifecycleShutdown()

    exit(0)


if __name__ == '__main__':
    main()