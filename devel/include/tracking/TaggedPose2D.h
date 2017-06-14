// Generated by gencpp from file tracking/TaggedPose2D.msg
// DO NOT EDIT!


#ifndef TRACKING_MESSAGE_TAGGEDPOSE2D_H
#define TRACKING_MESSAGE_TAGGEDPOSE2D_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace tracking
{
template <class ContainerAllocator>
struct TaggedPose2D_
{
  typedef TaggedPose2D_<ContainerAllocator> Type;

  TaggedPose2D_()
    : header()
    , id()
    , x(0.0)
    , y(0.0)
    , theta(0.0)
    , quality(0.0)  {
    }
  TaggedPose2D_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , id(_alloc)
    , x(0.0)
    , y(0.0)
    , theta(0.0)
    , quality(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _id_type;
  _id_type id;

   typedef double _x_type;
  _x_type x;

   typedef double _y_type;
  _y_type y;

   typedef double _theta_type;
  _theta_type theta;

   typedef double _quality_type;
  _quality_type quality;




  typedef boost::shared_ptr< ::tracking::TaggedPose2D_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tracking::TaggedPose2D_<ContainerAllocator> const> ConstPtr;

}; // struct TaggedPose2D_

typedef ::tracking::TaggedPose2D_<std::allocator<void> > TaggedPose2D;

typedef boost::shared_ptr< ::tracking::TaggedPose2D > TaggedPose2DPtr;
typedef boost::shared_ptr< ::tracking::TaggedPose2D const> TaggedPose2DConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::tracking::TaggedPose2D_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::tracking::TaggedPose2D_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace tracking

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'tracking': ['/home/finken/Development/paparazzi_SBE/catkin_ws/src/CameraTracking/tracking/msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::tracking::TaggedPose2D_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tracking::TaggedPose2D_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tracking::TaggedPose2D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tracking::TaggedPose2D_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tracking::TaggedPose2D_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tracking::TaggedPose2D_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::tracking::TaggedPose2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1195e3897a4e372a14daad5847c14708";
  }

  static const char* value(const ::tracking::TaggedPose2D_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1195e3897a4e372aULL;
  static const uint64_t static_value2 = 0x14daad5847c14708ULL;
};

template<class ContainerAllocator>
struct DataType< ::tracking::TaggedPose2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "tracking/TaggedPose2D";
  }

  static const char* value(const ::tracking::TaggedPose2D_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::tracking::TaggedPose2D_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
string id\n\
float64 x\n\
float64 y\n\
float64 theta\n\
float64 quality\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::tracking::TaggedPose2D_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::tracking::TaggedPose2D_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.id);
      stream.next(m.x);
      stream.next(m.y);
      stream.next(m.theta);
      stream.next(m.quality);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct TaggedPose2D_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tracking::TaggedPose2D_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::tracking::TaggedPose2D_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "id: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.id);
    s << indent << "x: ";
    Printer<double>::stream(s, indent + "  ", v.x);
    s << indent << "y: ";
    Printer<double>::stream(s, indent + "  ", v.y);
    s << indent << "theta: ";
    Printer<double>::stream(s, indent + "  ", v.theta);
    s << indent << "quality: ";
    Printer<double>::stream(s, indent + "  ", v.quality);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TRACKING_MESSAGE_TAGGEDPOSE2D_H
