from launch import LaunchDescription
from launch_ros.actions import Node   
from ament_index_python.packages import get_package_share_directory 
import os    

config_dir = os.path.join(get_package_share_directory('autonomous_tb3'), 'config') 
# The path we are trying to get in the above line of code is : "autonomous_maze_solving_turtlebot3/install/autonomous_tb3/share/autonomous_tb3/config"                              

def generate_launch_description():
    
    return LaunchDescription([
        Node(
            package="cartographer_ros",                       
            executable="cartographer_node",                  
            name="cart_node",   # node name can be anything of your choice
            arguments=["-configuration_directory", config_dir, "-configuration_basename", "turtlebot3_cartographer.lua"],                         
            output="screen"
        ),
        
        Node(
            package="cartographer_ros",
            executable="cartographer_occupancy_grid_node",
            name="cart_og_node",    # node name can be anything of your choice
            output="screen"
        ),
                        
    ])