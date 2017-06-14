
(cl:in-package :asdf)

(defsystem "tracking-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "TaggedPose2D" :depends-on ("_package_TaggedPose2D"))
    (:file "_package_TaggedPose2D" :depends-on ("_package"))
  ))