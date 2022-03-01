#!/usr/bin/python3
# #!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
import numpy as np
from rover_msgs.srv import WayPoints_srv_Tao
from rover_msgs.msg import WayPoints_msg_Tao

def routePlanner_client(Start, Target):
    rospy.wait_for_service('routePlanner')
    try:
        routePlanner = rospy.ServiceProxy('routePlanner', WayPoints_srv_Tao)
        response = routePlanner(Start, Target)
        rospy.loginfo(response)
        return response.X, response.Y, response.Width
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    #print(sys.argv)
    if len(sys.argv) == 5:
        Start = [float(sys.argv[1]), float(sys.argv[2])]
        Target = [float(sys.argv[3]), float(sys.argv[4])]
        print(Start, Target)
    else:
        print("have error in input format???? TaoSHU")
        sys.exit(1)
    print("Requesting route calculation")
    print(routePlanner_client(Start, Target))
    print("Route been published")
    #print("Requesting %s+%s"%(x, y))
