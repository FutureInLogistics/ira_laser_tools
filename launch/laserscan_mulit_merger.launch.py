import os

from ament_index_python import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import LifecycleNode
from launch.actions import EmitEvent
from launch.actions import RegisterEventHandler
from launch_ros.events.lifecycle import ChangeState
from launch_ros.events.lifecycle import matches_node_name
from launch_ros.event_handlers import OnStateTransition
from launch.events import matches_action


# <launch>
# 	<node pkg="ira_laser_tools" name="laserscan_multi_merger" exec="laserscan_multi_merger" output="screen">
# 		<param name="destination_frame" value="base_footprint"/>
# 		<param name="cloud_destination_topic" value="/merged_cloud"/>
# 		<param name="scan_destination_topic" value="/scan_multi"/>
# 		<param name="laserscan_topics" value ="/scan_back /scan_front" />
# 		<param name="angle_min" value="-3.14"/>
# 		<param name="angle_max" value="3.14"/>
# 		<param name="angle_increment" value="0.01178097166121"/>
# 		<param name="scan_time" value="0.0"/>
# 		<param name="range_min" value="0.1"/>
# 		<param name="range_max" value="20.0"/>
#     <param name="use_sim_time" value="false"/>
# 	</node>
# </launch>



def generate_launch_description():

  # odom 2 tf
  mulit_merger_node = Node(package='ira_laser_tools',
                           namespace='',
                           executable='laserscan_multi_merger',
                           name='laserscan_multi_merger',
                           output='screen',
                           parameters=[{
                             "destination_frame"       : "base_footprint",
                             "cloud_destination_topic" : "/merged_cloud",
                             "scan_destination_topic"  : "/scan_multi",
                             "laserscan_topics"        : "/scan_back /scan_front" ,
                             "angle_min"               : -3.14,
                             "angle_max"               : 3.14,
                             "angle_increment"         : 0.01178097166121,
                             "scan_time"               : 0.0,
                             "range_min"               : 0.1,
                             "range_max"               : 20.0,
                             # "param" : 1.0,
                             "use_sim_time": True
                           }],
                          #  remappings=[
                          #    ('/odom', '/odom'),
                          #  ]
                           )

  return LaunchDescription([
    mulit_merger_node
  ])