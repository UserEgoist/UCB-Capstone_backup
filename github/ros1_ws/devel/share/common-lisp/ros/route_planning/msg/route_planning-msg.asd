
(cl:in-package :asdf)

(defsystem "route_planning-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "WayPoints_Tao" :depends-on ("_package_WayPoints_Tao"))
    (:file "_package_WayPoints_Tao" :depends-on ("_package"))
  ))