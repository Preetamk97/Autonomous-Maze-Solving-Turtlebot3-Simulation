#! /usr/bin/env python3

# Node for spawning our maze world inside the gazebo simulation environment.

import sys
import rclpy
from gazebo_msgs.srv import SpawnEntity

def main():
    # Get input arguments from user
    argv = sys.argv[1:]
    
    # Starting the node
    rclpy.init()
    node = rclpy.create_node('spawning_node')
    node.get_logger().info(
        'Creating Service client to connect to `/spawn_entity`')
    client = node.create_client(SpawnEntity, '/spawn_entity')
    node.get_logger().info("Connecting to `/spawn_entity` service...")
    if not client.service_is_ready():
        client.wait_for_service()
        node.get_logger().info('..connected!')
    
    # Setting data for request
    # These data regarding the model will be provided along with the terminal command for starting the entity_spawner node - as arguments.
    request = SpawnEntity.Request()
    sdf_path = argv[0]  # location of .sdf file of the spawning model.
    request.name = argv[1]   # given name for the spawining model - can be found in 'model.config' file.
    request.xml = open(sdf_path, 'r').read()
    request.initial_pose.position.x = float(argv[2])  # x-coodinate for spawing the model in gazebo environment.
    request.initial_pose.position.y = float(argv[3])  # y-coodinate for spawing the model in gazebo environment.
    
    node.get_logger().info('Sending service request to /spawn_entity')
    future = client.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    if future.result() is not None:
        print('response: %r' % future.result())
    else:
        raise RuntimeError(
            'exceprion while calling service: %r' % future.exception()
        )
    node.get_logger().info('Done! Shutting down node.')
    node.destroy_node()
    rclpy.shutdown()
    

if __name__ == '__main__':
    main()