;; Auto-generated. Do not edit!


(when (boundp 'rover_msgs::WayPoints_srv_Tao)
  (if (not (find-package "ROVER_MSGS"))
    (make-package "ROVER_MSGS"))
  (shadow 'WayPoints_srv_Tao (find-package "ROVER_MSGS")))
(unless (find-package "ROVER_MSGS::WAYPOINTS_SRV_TAO")
  (make-package "ROVER_MSGS::WAYPOINTS_SRV_TAO"))
(unless (find-package "ROVER_MSGS::WAYPOINTS_SRV_TAOREQUEST")
  (make-package "ROVER_MSGS::WAYPOINTS_SRV_TAOREQUEST"))
(unless (find-package "ROVER_MSGS::WAYPOINTS_SRV_TAORESPONSE")
  (make-package "ROVER_MSGS::WAYPOINTS_SRV_TAORESPONSE"))

(in-package "ROS")





(defclass rover_msgs::WayPoints_srv_TaoRequest
  :super ros::object
  :slots (_Start _Target ))

(defmethod rover_msgs::WayPoints_srv_TaoRequest
  (:init
   (&key
    ((:Start __Start) (make-array 2 :initial-element 0.0 :element-type :float))
    ((:Target __Target) (make-array 2 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _Start __Start)
   (setq _Target __Target)
   self)
  (:Start
   (&optional __Start)
   (if __Start (setq _Start __Start)) _Start)
  (:Target
   (&optional __Target)
   (if __Target (setq _Target __Target)) _Target)
  (:serialization-length
   ()
   (+
    ;; float64[2] _Start
    (* 8    2)
    ;; float64[2] _Target
    (* 8    2)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[2] _Start
     (dotimes (i 2)
       (sys::poke (elt _Start i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[2] _Target
     (dotimes (i 2)
       (sys::poke (elt _Target i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[2] _Start
   (dotimes (i (length _Start))
     (setf (elt _Start i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;; float64[2] _Target
   (dotimes (i (length _Target))
     (setf (elt _Target i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     )
   ;;
   self)
  )

(defclass rover_msgs::WayPoints_srv_TaoResponse
  :super ros::object
  :slots (_X _Y _Width ))

(defmethod rover_msgs::WayPoints_srv_TaoResponse
  (:init
   (&key
    ((:X __X) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:Y __Y) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:Width __Width) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _X __X)
   (setq _Y __Y)
   (setq _Width __Width)
   self)
  (:X
   (&optional __X)
   (if __X (setq _X __X)) _X)
  (:Y
   (&optional __Y)
   (if __Y (setq _Y __Y)) _Y)
  (:Width
   (&optional __Width)
   (if __Width (setq _Width __Width)) _Width)
  (:serialization-length
   ()
   (+
    ;; float64[] _X
    (* 8    (length _X)) 4
    ;; float64[] _Y
    (* 8    (length _Y)) 4
    ;; float64[] _Width
    (* 8    (length _Width)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _X
     (write-long (length _X) s)
     (dotimes (i (length _X))
       (sys::poke (elt _X i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _Y
     (write-long (length _Y) s)
     (dotimes (i (length _Y))
       (sys::poke (elt _Y i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _Width
     (write-long (length _Width) s)
     (dotimes (i (length _Width))
       (sys::poke (elt _Width i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _X
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _X (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _X i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _Y
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _Y (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _Y i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _Width
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _Width (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _Width i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass rover_msgs::WayPoints_srv_Tao
  :super ros::object
  :slots ())

(setf (get rover_msgs::WayPoints_srv_Tao :md5sum-) "f979d4bef44161c3de0eaa389ab41bd3")
(setf (get rover_msgs::WayPoints_srv_Tao :datatype-) "rover_msgs/WayPoints_srv_Tao")
(setf (get rover_msgs::WayPoints_srv_Tao :request) rover_msgs::WayPoints_srv_TaoRequest)
(setf (get rover_msgs::WayPoints_srv_Tao :response) rover_msgs::WayPoints_srv_TaoResponse)

(defmethod rover_msgs::WayPoints_srv_TaoRequest
  (:response () (instance rover_msgs::WayPoints_srv_TaoResponse :init)))

(setf (get rover_msgs::WayPoints_srv_TaoRequest :md5sum-) "f979d4bef44161c3de0eaa389ab41bd3")
(setf (get rover_msgs::WayPoints_srv_TaoRequest :datatype-) "rover_msgs/WayPoints_srv_TaoRequest")
(setf (get rover_msgs::WayPoints_srv_TaoRequest :definition-)
      "float64[2] Start
float64[2] Target
---
float64[] X
float64[] Y
float64[] Width


")

(setf (get rover_msgs::WayPoints_srv_TaoResponse :md5sum-) "f979d4bef44161c3de0eaa389ab41bd3")
(setf (get rover_msgs::WayPoints_srv_TaoResponse :datatype-) "rover_msgs/WayPoints_srv_TaoResponse")
(setf (get rover_msgs::WayPoints_srv_TaoResponse :definition-)
      "float64[2] Start
float64[2] Target
---
float64[] X
float64[] Y
float64[] Width


")



(provide :rover_msgs/WayPoints_srv_Tao "f979d4bef44161c3de0eaa389ab41bd3")


