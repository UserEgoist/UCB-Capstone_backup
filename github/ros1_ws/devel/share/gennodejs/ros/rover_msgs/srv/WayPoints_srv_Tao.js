// Auto-generated. Do not edit!

// (in-package rover_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class WayPoints_srv_TaoRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Start = null;
      this.Target = null;
    }
    else {
      if (initObj.hasOwnProperty('Start')) {
        this.Start = initObj.Start
      }
      else {
        this.Start = new Array(2).fill(0);
      }
      if (initObj.hasOwnProperty('Target')) {
        this.Target = initObj.Target
      }
      else {
        this.Target = new Array(2).fill(0);
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type WayPoints_srv_TaoRequest
    // Check that the constant length array field [Start] has the right length
    if (obj.Start.length !== 2) {
      throw new Error('Unable to serialize array field Start - length must be 2')
    }
    // Serialize message field [Start]
    bufferOffset = _arraySerializer.float64(obj.Start, buffer, bufferOffset, 2);
    // Check that the constant length array field [Target] has the right length
    if (obj.Target.length !== 2) {
      throw new Error('Unable to serialize array field Target - length must be 2')
    }
    // Serialize message field [Target]
    bufferOffset = _arraySerializer.float64(obj.Target, buffer, bufferOffset, 2);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WayPoints_srv_TaoRequest
    let len;
    let data = new WayPoints_srv_TaoRequest(null);
    // Deserialize message field [Start]
    data.Start = _arrayDeserializer.float64(buffer, bufferOffset, 2)
    // Deserialize message field [Target]
    data.Target = _arrayDeserializer.float64(buffer, bufferOffset, 2)
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a service object
    return 'rover_msgs/WayPoints_srv_TaoRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '02ca451f5485348f989a305e0bc6aad0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[2] Start
    float64[2] Target
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new WayPoints_srv_TaoRequest(null);
    if (msg.Start !== undefined) {
      resolved.Start = msg.Start;
    }
    else {
      resolved.Start = new Array(2).fill(0)
    }

    if (msg.Target !== undefined) {
      resolved.Target = msg.Target;
    }
    else {
      resolved.Target = new Array(2).fill(0)
    }

    return resolved;
    }
};

class WayPoints_srv_TaoResponse {
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
    // Serializes a message object of type WayPoints_srv_TaoResponse
    // Serialize message field [X]
    bufferOffset = _arraySerializer.float64(obj.X, buffer, bufferOffset, null);
    // Serialize message field [Y]
    bufferOffset = _arraySerializer.float64(obj.Y, buffer, bufferOffset, null);
    // Serialize message field [Width]
    bufferOffset = _arraySerializer.float64(obj.Width, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type WayPoints_srv_TaoResponse
    let len;
    let data = new WayPoints_srv_TaoResponse(null);
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
    // Returns string type for a service object
    return 'rover_msgs/WayPoints_srv_TaoResponse';
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
    const resolved = new WayPoints_srv_TaoResponse(null);
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

module.exports = {
  Request: WayPoints_srv_TaoRequest,
  Response: WayPoints_srv_TaoResponse,
  md5sum() { return 'f979d4bef44161c3de0eaa389ab41bd3'; },
  datatype() { return 'rover_msgs/WayPoints_srv_Tao'; }
};
