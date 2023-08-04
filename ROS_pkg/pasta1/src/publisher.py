#!/usr/bin/env python3
# license removed for brevity
import rospy
import random
from std_msgs.msg import String
from pasta1.msg import Velocity

def talker():
    pub = rospy.Publisher('chatter', Velocity, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg = Velocity()
        msg.time = rospy.get_time()
        msg.vel_lin_x = random.randint(0, 100)
        msg.vel_lin_y = random.randint(0, 100)
        msg.vel_lin_z = random.randint(0, 100)
        msg.vel_ang_x = random.randint(0, 360)
        msg.vel_ang_y = random.randint(0, 360)
        msg.vel_ang_z = random.randint(0, 360)
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass