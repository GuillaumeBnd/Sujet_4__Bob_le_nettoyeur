; Auto-generated. Do not edit!


(cl:in-package detection-msg)


;//! \htmlinclude Vide.msg.html

(cl:defclass <Vide> (roslisp-msg-protocol:ros-message)
  ((detected
    :reader detected
    :initarg :detected
    :type cl:integer
    :initform 0))
)

(cl:defclass Vide (<Vide>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Vide>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Vide)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name detection-msg:<Vide> is deprecated: use detection-msg:Vide instead.")))

(cl:ensure-generic-function 'detected-val :lambda-list '(m))
(cl:defmethod detected-val ((m <Vide>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader detection-msg:detected-val is deprecated.  Use detection-msg:detected instead.")
  (detected m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Vide>) ostream)
  "Serializes a message object of type '<Vide>"
  (cl:let* ((signed (cl:slot-value msg 'detected)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Vide>) istream)
  "Deserializes a message object of type '<Vide>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'detected) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Vide>)))
  "Returns string type for a message object of type '<Vide>"
  "detection/Vide")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Vide)))
  "Returns string type for a message object of type 'Vide"
  "detection/Vide")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Vide>)))
  "Returns md5sum for a message object of type '<Vide>"
  "23f88efd171b2e5dc0ad9793b17bca9d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Vide)))
  "Returns md5sum for a message object of type 'Vide"
  "23f88efd171b2e5dc0ad9793b17bca9d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Vide>)))
  "Returns full string definition for message of type '<Vide>"
  (cl:format cl:nil "int64 detected~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Vide)))
  "Returns full string definition for message of type 'Vide"
  (cl:format cl:nil "int64 detected~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Vide>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Vide>))
  "Converts a ROS message object to a list"
  (cl:list 'Vide
    (cl:cons ':detected (detected msg))
))
