#!/usr/bin/env python3

import rospy
import tf2_ros
import yaml
import math
from tf2_geometry_msgs import PointStamped

def load_parameters():
    with open(rospy.get_param("sistema_solar_params_path"), 'r') as file:
        return yaml.safe_load(file)

def broadcast_transforms():
    params = load_parameters()

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    tf_broadcaster = tf2_ros.TransformBroadcaster()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            for planeta in params['planetas']:
                # Transformação da estrela para o planeta
                transform = tf_buffer.lookup_transform(
                    params['estrela'], planeta['nome'], rospy.Time())
                tf_broadcaster.sendTransform(transform)

                # Transformações dos satélites para o planeta
                for satelite in planeta.get('satelites', []):
                    transform = tf_buffer.lookup_transform(
                        planeta['nome'], satelite['nome'], rospy.Time())
                    tf_broadcaster.sendTransform(transform)
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException,
                tf2_ros.ExtrapolationException):
            pass

        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('sistema_solar')

    # Carregar parâmetros
    params_path = rospy.get_param("~params_path", "config/sistema_solar_params.yaml")
    rospy.set_param("sistema_solar_params_path", params_path)

    broadcast_transforms()
