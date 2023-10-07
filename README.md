# Autonomous Maze Solving Turtlebot3 Simulation

This repository contains the code to produce a **Gazebo Classic Simulation** of a **Turtlebot3** (***waffle***) robot (designed by *Robotis*) that navigates its way through a simple maze **autonomously**.

This repository was built while following the learnings and instructions of the **Udemy** Course **ROS2 Autonomous Driving and SLAM using NAV2 with TurtleBot3** created by **Muhammad Luqman**.

The software tools mainly used in building this project are :

- Python3 Interpreter
- Basic ROS2 Framework
- Gazebo Classic Simulator
- *turtlebot3_gazebo* ROS2 package
- *slam_toolbox* ROS2 package
- Navigation2 Stack

Operating System :
- Ubuntu (*you can use the latest version available*) 

In order to deploy this project successfully, all the above listed softwares must be installed in your Ubuntu OS.


## What is DIFFERENT in this Project ? 

Originally, this project was built as an **ament_python** type ROS2 package in the above mentioned Course. However, in this repository, I have built the project as an **ament_cmake** type ROS2 package.


## Deployment

To deploy this project, please follow the below mentioned steps.

- **Create a new folder** at a suitable space in your Ubuntu OS. You can name the folder anything you want. But for the sake of this demonstration, I am naming it as **Cloned Repo**

- Open a **new terminal** inside the folder.

- **Clone this repository** inside the folder by running the following terminal command.

    ```bash
    git clone https://github.com/Preetamk97/Autonomous-Maze-Solving-Turtlebot3-Simulation.git
    ```

- This will create a new folder named **Autonomous-Maze-Solving-Turtlebot3-Simulation** inside the **Cloned Repo** directory.

- Go inside the **Autonomous-Maze-Solving-Turtlebot3-Simulation** folder through the previously opened terminal.

    ```
    cd Autonomous-Maze-Solving-Turtlebot3-Simulation/
    ```

- Next, we need to build this project. So run the following command from the same terminal.

    ```bash
    colcon build
    ```
    
    This will generate 3 (three) new folders inside the **Autonomous Maze Solving Turtlebot3 Simulation** folder namely - **build**, **install** and **log**.

- Close the previous terminal.

- Next, finally we can deploy the project.
    
    - Open a new terminal inside the **Autonomous Maze Solving Turtlebot3 Simulation** directory and run the following commands:
        ```bash
        source install/setup.bash
        ros2 launch autonomous_tb3 tb3_maze_navigation.launch.py
        ```

        This will open a **Gazebo Classic Simulator Window** (with the simulated ***maze world*** and a ***Turtlebot3*** robot - inside of it) AND a **RViz2 Window** (where you can see a 2D map of the maze world). 
        
        Use ***Mouse Scroll Wheel*** to ***Zoom IN/Zoom OUT*** in both the **Gazebo** and **RViz2** enviroments.

        Use **left mouse button** (to PAN) and ***Mouse Scroll Button*** (to ROTATE) -- for adjusting the position and view of the **maze world** in the **Gazebo** environment - as per your convenience.

        Use **left mouse button** (to ROTATE) and ***Mouse Scroll Button*** (to PAN) -- for adjusting the position and view of the **2D maze map** in the **RViz2** environment - a per your convenience.

        Also, before proceeding to the next step, it is recomended to keep both the **Gazebo** and **Rviz2** windows opened side by side, so that you that you can see see what's happening in both the windows at the same time.

    - Open a second parallel terminal inside the **Autonomous Maze Solving Turtlebot3 Simulation** directory (while keeping the previous terminal alive) and run the following command from it :
        ```bash
        source install/setup.bash
        ros2 run autonomous_tb3 maze_solver.py
        ```


## Output

Once you have followed all the mentioned steps inside the **Deployment** section, the following **simulation output** can be seen in the **Gazebo Classic Simulator** window.

<figure class="video_container">
  <video controls="true" allowfullscreen="true" poster="Thumbnail.png">
    <source src="Gazebo_Sim_Recording.mp4" type="video/mp4">
  </video>
</figure>

You can also see the robot following ***the same*** trajectory in the ***2D maze map*** of the **RViz2** environment simultaneously. I could not screen record the **RViz2** simulation to show you - due to my computer hardware limitations.


## References

- [ROS2 Autonomous Driving and SLAM using NAV2 with TurtleBot3 : Udemy Course by Muhammad Luqman](https://www.udemy.com/course/robotics-with-ros-autonomous-driving-and-path-planning-slam/?utm_source=adwords&utm_medium=udemyads&utm_campaign=DSA_Catchall_la.EN_cc.INDIA&utm_content=deal4584&utm_term=_._ag_82569850245_._ad_533220805574_._kw__._de_c_._dm__._pl__._ti_dsa-406594358574_._li_9180185_._pd__._&matchtype=&gclid=CjwKCAjwg4SpBhAKEiwAdyLwvN8lgU-i14AFswYX5PRxoyyk4vTsQTeZowGazBI_IPSTdqcZ9TntWxoCGxUQAvD_BwE)
- [Official Github Account of Robotis: ROBOTIS-GIT](https://github.com/ROBOTIS-GIT)
- [Official Github Account of ROS Planning: ros-planning ](https://github.com/ros-planning)
 
