#!/usr/bin/env python3
import rospy
import math
from std_msgs.msg import String
from pasta1.msg import Velocity
from pasta1.msg import Modulo

def callback(data):
    msg = Modulo()
    pub_modulo = rospy.Publisher('modulos: ', Modulo, queue_size=10)
    msg.modulo_lin = math.sqrt(math.pow(data.vel_lin_x, 2) + math.pow(data.vel_lin_y, 2) + math.pow(data.vel_lin_z, 2))
    msg.modulo_ang = math.sqrt(math.pow(data.vel_ang_x, 2) + math.pow(data.vel_ang_y, 2) + math.pow(data.vel_ang_z, 2))
    rospy.loginfo(rospy.get_caller_id() + "modulo da velocidade linear = %s" % msg.modulo_ang)
    rospy.loginfo(rospy.get_caller_id() + "modulo da velocidade angular = %s" % msg.modulo_lin)
    pub_modulo.publish(msg)
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Velocity, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()