// Auto-generated. Do not edit!

// (in-package rover_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class WayPoints_msg_Tao {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.X = null;
      this.Y = null;
      this.Width = null;
    }
    else {
      if (initObj.hasOwnProperty('X')) {
        this.X = initObj.X
      }
      else {
        this.X = [];
      }
      if (initObj.hasOwnProperty('Y')) {
        this.Y = initObj.Y
      }
      else {
        this.Y = [];
      }
      if (initObj.hasOwnProperty('Width')) {
        this.Width = initObj.Width
      }
      else {
        this.Width = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WayPoints_msg_Tao
    // Serialize message field [X]
    bufferOffset = _arraySerializer.float64(obj.X, buffer, bufferOffset, null);
    // Serialize message field [Y]
    bufferOffset = _arraySerializer.float64(obj.Y, buffer, bufferOffset, null);
    // Serialize message field [Width]
    bufferOffset = _arraySerializer.float64(obj.Width, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WayPoints_msg_Tao
    let len;
    let data = new WayPoints_msg_Tao(null);
    // Deserialize message field [X]
    data.X = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [Y]
    data.Y = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [Width]
    data.Width = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.X.length;
    length += 8 * object.Y.length;
    length += 8 * object.Width.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'rover_msgs/WayPoints_msg_Tao';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '2cf425913cc89fed1c98af7ab0af40fa';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] X
    float64[] Y
    float64[] Width
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WayPoints_msg_Tao(null);
    if (msg.X !== undefined) {
      resolved.X = msg.X;
    }
    else {
      resolved.X = []
    }

    if (msg.Y !== undefined) {
      resolved.Y = msg.Y;
    }
    else {
      resolved.Y = []
    }

    if (msg.Width !== undefined) {
      resolved.Width = msg.Width;
    }
    else {
      resolved.Width = []
    }

    return resolved;
    }
};

module.exports = WayPoints_msg_Tao;
