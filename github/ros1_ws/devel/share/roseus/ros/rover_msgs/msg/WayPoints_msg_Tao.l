;; Auto-generated. Do not edit!


(when (boundp 'rover_msgs::WayPoints_msg_Tao)
  (if (not (find-package "ROVER_MSGS"))
    (make-package "ROVER_MSGS"))
  (shadow 'WayPoints_msg_Tao (find-package "ROVER_MSGS")))
(unless (find-package "ROVER_MSGS::WAYPOINTS_MSG_TAO")
  (make-package "ROVER_MSGS::WAYPOINTS_MSG_TAO"))

(in-package "ROS")
;;//! \htmlinclude WayPoints_msg_Tao.msg.html


(defclass rover_msgs::WayPoints_msg_Tao
  :super ros::object
  :slots (_X _Y _Width ))

(defmethod rover_msgs::WayPoints_msg_Tao
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

(setf (get rover_msgs::WayPoints_msg_Tao :md5sum-) "2cf425913cc89fed1c98af7ab0af40fa")
(setf (get rover_msgs::WayPoints_msg_Tao :datatype-) "rover_msgs/WayPoints_msg_Tao")
(setf (get rover_msgs::WayPoints_msg_Tao :definition-)
      "float64[] X
float64[] Y
float64[] Width


")



(provide :rover_msgs/WayPoints_msg_Tao "2cf425913cc89fed1c98af7ab0af40fa")

