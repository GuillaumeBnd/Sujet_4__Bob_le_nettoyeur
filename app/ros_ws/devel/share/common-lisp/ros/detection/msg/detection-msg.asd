
(cl:in-package :asdf)

(defsystem "detection-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Vide" :depends-on ("_package_Vide"))
    (:file "_package_Vide" :depends-on ("_package"))
  ))