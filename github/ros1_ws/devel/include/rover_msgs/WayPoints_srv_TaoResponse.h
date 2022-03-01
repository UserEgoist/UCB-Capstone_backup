// Generated by gencpp from file rover_msgs/WayPoints_srv_TaoResponse.msg
// DO NOT EDIT!


#ifndef ROVER_MSGS_MESSAGE_WAYPOINTS_SRV_TAORESPONSE_H
#define ROVER_MSGS_MESSAGE_WAYPOINTS_SRV_TAORESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rover_msgs
{
template <class ContainerAllocator>
struct WayPoints_srv_TaoResponse_
{
  typedef WayPoints_srv_TaoResponse_<ContainerAllocator> Type;

  WayPoints_srv_TaoResponse_()
    : X()
    , Y()
    , Width()  {
    }
  WayPoints_srv_TaoResponse_(const ContainerAllocator& _alloc)
    : X(_alloc)
    , Y(_alloc)
    , Width(_alloc)  {
  (void)_alloc;
    }



   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _X_type;
  _X_type X;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _Y_type;
  _Y_type Y;

   typedef std::vector<double, typename ContainerAllocator::template rebind<double>::other >  _Width_type;
  _Width_type Width;





  typedef boost::shared_ptr< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> const> ConstPtr;

}; // struct WayPoints_srv_TaoResponse_

typedef ::rover_msgs::WayPoints_srv_TaoResponse_<std::allocator<void> > WayPoints_srv_TaoResponse;

typedef boost::shared_ptr< ::rover_msgs::WayPoints_srv_TaoResponse > WayPoints_srv_TaoResponsePtr;
typedef boost::shared_ptr< ::rover_msgs::WayPoints_srv_TaoResponse const> WayPoints_srv_TaoResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator1> & lhs, const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator2> & rhs)
{
  return lhs.X == rhs.X &&
    lhs.Y == rhs.Y &&
    lhs.Width == rhs.Width;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator1> & lhs, const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rover_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2cf425913cc89fed1c98af7ab0af40fa";
  }

  static const char* value(const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2cf425913cc89fedULL;
  static const uint64_t static_value2 = 0x1c98af7ab0af40faULL;
};

template<class ContainerAllocator>
struct DataType< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rover_msgs/WayPoints_srv_TaoResponse";
  }

  static const char* value(const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64[] X\n"
"float64[] Y\n"
"float64[] Width\n"
"\n"
"\n"
;
  }

  static const char* value(const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.X);
      stream.next(m.Y);
      stream.next(m.Width);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct WayPoints_srv_TaoResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rover_msgs::WayPoints_srv_TaoResponse_<ContainerAllocator>& v)
  {
    s << indent << "X[]" << std::endl;
    for (size_t i = 0; i < v.X.size(); ++i)
    {
      s << indent << "  X[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.X[i]);
    }
    s << indent << "Y[]" << std::endl;
    for (size_t i = 0; i < v.Y.size(); ++i)
    {
      s << indent << "  Y[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.Y[i]);
    }
    s << indent << "Width[]" << std::endl;
    for (size_t i = 0; i < v.Width.size(); ++i)
    {
      s << indent << "  Width[" << i << "]: ";
      Printer<double>::stream(s, indent + "  ", v.Width[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROVER_MSGS_MESSAGE_WAYPOINTS_SRV_TAORESPONSE_H
