// Generated by gencpp from file lidar_cluster/pointcloud_cluster.msg
// DO NOT EDIT!


#ifndef LIDAR_CLUSTER_MESSAGE_POINTCLOUD_CLUSTER_H
#define LIDAR_CLUSTER_MESSAGE_POINTCLOUD_CLUSTER_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <sensor_msgs/PointCloud2.h>

namespace lidar_cluster
{
template <class ContainerAllocator>
struct pointcloud_cluster_
{
  typedef pointcloud_cluster_<ContainerAllocator> Type;

  pointcloud_cluster_()
    : header()
    , cluster()  {
    }
  pointcloud_cluster_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , cluster(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef std::vector< ::sensor_msgs::PointCloud2_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::sensor_msgs::PointCloud2_<ContainerAllocator> >::other >  _cluster_type;
  _cluster_type cluster;





  typedef boost::shared_ptr< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> const> ConstPtr;

}; // struct pointcloud_cluster_

typedef ::lidar_cluster::pointcloud_cluster_<std::allocator<void> > pointcloud_cluster;

typedef boost::shared_ptr< ::lidar_cluster::pointcloud_cluster > pointcloud_clusterPtr;
typedef boost::shared_ptr< ::lidar_cluster::pointcloud_cluster const> pointcloud_clusterConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator1> & lhs, const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator2> & rhs)
{
  return lhs.header == rhs.header &&
    lhs.cluster == rhs.cluster;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator1> & lhs, const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace lidar_cluster

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "03cc5f413fedb5e9b5520c03d0e6e027";
  }

  static const char* value(const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x03cc5f413fedb5e9ULL;
  static const uint64_t static_value2 = 0xb5520c03d0e6e027ULL;
};

template<class ContainerAllocator>
struct DataType< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "lidar_cluster/pointcloud_cluster";
  }

  static const char* value(const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# Pointcloud Cluster Msg\n"
"\n"
"Header header\n"
"sensor_msgs/PointCloud2[] cluster\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/PointCloud2\n"
"# This message holds a collection of N-dimensional points, which may\n"
"# contain additional information such as normals, intensity, etc. The\n"
"# point data is stored as a binary blob, its layout described by the\n"
"# contents of the \"fields\" array.\n"
"\n"
"# The point cloud data may be organized 2d (image-like) or 1d\n"
"# (unordered). Point clouds organized as 2d images may be produced by\n"
"# camera depth sensors such as stereo or time-of-flight.\n"
"\n"
"# Time of sensor data acquisition, and the coordinate frame ID (for 3d\n"
"# points).\n"
"Header header\n"
"\n"
"# 2D structure of the point cloud. If the cloud is unordered, height is\n"
"# 1 and width is the length of the point cloud.\n"
"uint32 height\n"
"uint32 width\n"
"\n"
"# Describes the channels and their layout in the binary data blob.\n"
"PointField[] fields\n"
"\n"
"bool    is_bigendian # Is this data bigendian?\n"
"uint32  point_step   # Length of a point in bytes\n"
"uint32  row_step     # Length of a row in bytes\n"
"uint8[] data         # Actual point data, size is (row_step*height)\n"
"\n"
"bool is_dense        # True if there are no invalid points\n"
"\n"
"================================================================================\n"
"MSG: sensor_msgs/PointField\n"
"# This message holds the description of one point entry in the\n"
"# PointCloud2 message format.\n"
"uint8 INT8    = 1\n"
"uint8 UINT8   = 2\n"
"uint8 INT16   = 3\n"
"uint8 UINT16  = 4\n"
"uint8 INT32   = 5\n"
"uint8 UINT32  = 6\n"
"uint8 FLOAT32 = 7\n"
"uint8 FLOAT64 = 8\n"
"\n"
"string name      # Name of field\n"
"uint32 offset    # Offset from start of point struct\n"
"uint8  datatype  # Datatype enumeration, see above\n"
"uint32 count     # How many elements in the field\n"
;
  }

  static const char* value(const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.cluster);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct pointcloud_cluster_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::lidar_cluster::pointcloud_cluster_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::lidar_cluster::pointcloud_cluster_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "cluster[]" << std::endl;
    for (size_t i = 0; i < v.cluster.size(); ++i)
    {
      s << indent << "  cluster[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::sensor_msgs::PointCloud2_<ContainerAllocator> >::stream(s, indent + "    ", v.cluster[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // LIDAR_CLUSTER_MESSAGE_POINTCLOUD_CLUSTER_H
