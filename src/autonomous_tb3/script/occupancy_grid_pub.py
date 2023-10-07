#! /usr/bin/env python3

# Node for publishing the OccupancyGrid Messages.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
# Additional Imports
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Header
import numpy as np

# The OccupancyGrid message type of nav_msgs package, represents a grid map comprising of several square boxes. 
# Each square box of the map is represented by numbers 0, 1, -1.
# 0 represents unoccupied, 1 represents definitely occupied, and -1 represents unknown.

# To see the details of OccupancyGrid message type run the command 'ros2 interface show nav_msgs/msg/OccupancyGrid' from a terminal.

# Attributes of OccupancyGrid message datatype:

    # std_msgs/Header header
        # builtin_interfaces/Time stamp
        # 	int32 sec
        # 	uint32 nanosec
    
        # string frame_id

    # MapMetaData info
        # builtin_interfaces/Time map_load_time
        #     int32 sec
        #     uint32 nanosec
        # float32 resolution
        # uint32 width
        # uint32 height
        # geometry_msgs/Pose origin
        #     Point position
        #         float64 x
        #         float64 y
        #         float64 z
        #     Quaternion orientation
        #         float64 x
        #         float64 y
        #         float64 z
        #         float64 w

    # int8[] data

class Occupancy_Grid_Publisher(Node):

    def __init__(self):
        super().__init__('occupancy_grid_pub_node')
        self.publisher_ = self.create_publisher(OccupancyGrid, 'occupancy_grid_map', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        
    def timer_callback(self):
        # Initialising the publisher message which is of OccupancyGrid datatype.
        msg = OccupancyGrid()   
        
        # the header attribute of the message consists of a std_msgs/msg/Header type data. 
        msg.header = Header()  # Initailizing 
         
        # the 'std_msgs/msg/Header header' attribute consists of 2 propertise - 'builtin_interfaces/Time stamp' and 'string frame_id'.
        msg.header.stamp = self.get_clock().now().to_msg()   # current time
        msg.header.frame_id = 'map_frame'   # think of it as the name given to our map
             
        msg.info.resolution = 1.0
        msg.info.width = 3      # Our grid map will have 3 boxes on the x-axis direction 
        msg.info.height = 3     # Our grid map will have 3 boxes on the y-axis direction 
        # Below 3 values represents the origin position of our map (pose).
        msg.info.origin.position.x = 0.0
        msg.info.origin.position.y = 0.0
        msg.info.origin.position.z = 0.0
        
        # the 'data' attribute id the message, dictates which boxes of the grid are gonna be occupied and which boxes are gonna be un-occupied.
        msg.data = np.array([0,1,1,0,1,1,1,1,0], dtype=np.int8).tolist()
        #  ______ ______ ______
        # |      |      |      |
        # |   0  |  0   |  1   |
        # |______|______|______|
        # |      |      |      |
        # |   1  |  1   |  1   |
        # |______|______|______|
        # |      |      |      |
        # |   1  |  1   |  0   |
        # |______|______|______|
        
        # 0 represents unoccupied, 1 represents definitely occupied, and -1 represents unknown.
        
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    occupancy_grid_publisher = Occupancy_Grid_Publisher()
    print('Publishing Map...')
    rclpy.spin(occupancy_grid_publisher)
    occupancy_grid_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    
    
# To visualize the grid map that is being published by this publisher node:
    # open a terminal "from the workspace" (terminal 1) and run the following commands:
        #  source install/setup.bash
        #  ros2 run autonomous_tb3 occupancy_grid_pub.py
    # open another "general" terminal (terminal 2) and run the command `rviz2` to launch the rviz visualization tool.
    # Once you, open the rviz visualization tool:
        # In the left-side of the window, under the Displays > Global Options > Fixed Frame -- rewrite 'map' as 'map_frame' (which is the name of our grid map).
        # Search for and click on the 'Add' button at the bottom-left of the window. Add > rviz_default_plugins > Map > OK.
        # Under the Displays > Map > Set 'Topic' as 'occupancy_grid_map'
        # Again, under the Displays > Map > Set 'Color Scheme' as 'Cost Map'