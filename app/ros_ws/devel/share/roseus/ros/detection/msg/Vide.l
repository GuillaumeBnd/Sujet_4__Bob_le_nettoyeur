;; Auto-generated. Do not edit!


(when (boundp 'detection::Vide)
  (if (not (find-package "DETECTION"))
    (make-package "DETECTION"))
  (shadow 'Vide (find-package "DETECTION")))
(unless (find-package "DETECTION::VIDE")
  (make-package "DETECTION::VIDE"))

(in-package "ROS")
;;//! \htmlinclude Vide.msg.html


(defclass detection::Vide
  :super ros::object
  :slots (_detected ))

(defmethod detection::Vide
  (:init
   (&key
    ((:detected __detected) 0)
    )
   (send-super :init)
   (setq _detected (round __detected))
   self)
  (:detected
   (&optional __detected)
   (if __detected (setq _detected __detected)) _detected)
  (:serialization-length
   ()
   (+
    ;; int64 _detected
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _detected
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _detected (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _detected) (= (length (_detected . bv)) 2)) ;; bignum
              (write-long (ash (elt (_detected . bv) 0) 0) s)
              (write-long (ash (elt (_detected . bv) 1) -1) s))
             ((and (class _detected) (= (length (_detected . bv)) 1)) ;; big1
              (write-long (elt (_detected . bv) 0) s)
              (write-long (if (>= _detected 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _detected s)(write-long (if (>= _detected 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _detected
#+(or :alpha :irix6 :x86_64)
      (setf _detected (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _detected (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get detection::Vide :md5sum-) "23f88efd171b2e5dc0ad9793b17bca9d")
(setf (get detection::Vide :datatype-) "detection/Vide")
(setf (get detection::Vide :definition-)
      "int64 detected

")



(provide :detection/Vide "23f88efd171b2e5dc0ad9793b17bca9d")


