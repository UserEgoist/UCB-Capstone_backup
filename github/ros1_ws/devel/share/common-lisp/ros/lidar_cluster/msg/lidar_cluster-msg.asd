
(cl:in-package :asdf)

(defsystem "lidar_cluster-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "pointcloud_cluster" :depends-on ("_package_pointcloud_cluster"))
    (:file "_package_pointcloud_cluster" :depends-on ("_package"))
  ))