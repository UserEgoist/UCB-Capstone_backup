
(cl:in-package :asdf)

(defsystem "rover_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "WayPoints_msg_Tao" :depends-on ("_package_WayPoints_msg_Tao"))
    (:file "_package_WayPoints_msg_Tao" :depends-on ("_package"))
  ))