from launch import LaunchDescription
from launch_ros.actions import Node  
import os  
 
from ament_index_python.packages import get_package_share_directory 
from pathlib import Path

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import SetEnvironmentVariable

# Getting the required file paths
#-------------------------------------
config_dir_share_path = os.path.join(get_package_share_directory('autonomous_tb3'), 'config') 
# The path we are trying to get in the above line of code is : "autonomous_maze_solving_turtlebot3/install/autonomous_tb3/share/autonomous_tb3/config" 
map_config_file_path = os.path.join(config_dir_share_path, "tb3_world_2d_map.yaml")    
params_config_file_path = os.path.join(config_dir_share_path, "tb3_nav_params.yaml") 
rviz_config_file_path = os.path.join(config_dir_share_path, "tb3_nav.rviz")  
turtlebot3_gazebo_share_path = get_package_share_directory('turtlebot3_gazebo')
# The path we are trying to get in the above line of code is : "/opt/ros/humble/share/turtlebot3_gazebo"
nav2_bringup_share_path = get_package_share_directory('nav2_bringup')
# The path we are trying to get in the above line of code is : "/opt/ros/humble/share/nav2_bringup"
           

def generate_launch_description():
    
    return LaunchDescription([
        
        # Setting the type to turtlebot3 robot to be used in simulation.
        SetEnvironmentVariable(
            name = "TURTLEBOT3_MODEL",
            value="waffle"
        ),
        
        # Starting the turtlebot3 simulation  
        IncludeLaunchDescription(
             PythonLaunchDescriptionSource (
                 launch_file_path=Path(turtlebot3_gazebo_share_path, "launch/turtlebot3_world.launch.py").as_posix()
                # [turtlebot3_gazebo_share_path, '/launch', '/turtlebot3_world.launch.py']
                
                 # Using the 'turtlebot3_world.launch.py' file inside the 'launch' directory of the 'turtlebot3_gazebo' package's 'share' directory - for launching the simulation.
             )
         ),
        
        # Integrating Nav2 Stack : Launching the bringup_launch.py file
        IncludeLaunchDescription(
             PythonLaunchDescriptionSource (
                 launch_file_path=Path(nav2_bringup_share_path, "launch/bringup_launch.py").as_posix()
                 
                 # Using the 'bringup_launch.py' file inside the 'launch' directory of the 'nav2_bringup' package's 'share' directory - for using the Navigation2 stack with the project.
             ),
             launch_arguments = {
                 'map' : map_config_file_path,
                 'params_file' : params_config_file_path
                 }.items(),
         ),
        
        # Launching Rviz2
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2_node",    # node name can be anything of your choice
            arguments = ['-d', rviz_config_file_path],
            output="screen"
        )                     
    ])