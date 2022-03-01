
(cl:in-package :asdf)

(defsystem "rover_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "WayPoints_srv_Tao" :depends-on ("_package_WayPoints_srv_Tao"))
    (:file "_package_WayPoints_srv_Tao" :depends-on ("_package"))
  ))