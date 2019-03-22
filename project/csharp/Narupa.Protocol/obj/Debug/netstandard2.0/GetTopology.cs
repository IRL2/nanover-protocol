// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: narupa/protocol/instance/get_topology.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Narupa.Protocol.Instance {

  /// <summary>Holder for reflection information generated from narupa/protocol/instance/get_topology.proto</summary>
  public static partial class GetTopologyReflection {

    #region Descriptor
    /// <summary>File descriptor for narupa/protocol/instance/get_topology.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GetTopologyReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CituYXJ1cGEvcHJvdG9jb2wvaW5zdGFuY2UvZ2V0X3RvcG9sb2d5LnByb3Rv",
            "EhhuYXJ1cGEucHJvdG9jb2wuaW5zdGFuY2UaJ25hcnVwYS9wcm90b2NvbC90",
            "b3BvbG9neS90b3BvbG9neS5wcm90bxofbmFydXBhL3Byb3RvY29sL2RlbGlt",
            "aXRlci5wcm90byIUChJHZXRUb3BvbG9neVJlcXVlc3QikwEKE0dldFRvcG9s",
            "b2d5UmVzcG9uc2USEwoLZnJhbWVfaW5kZXgYASABKA0SOAoIdG9wb2xvZ3kY",
            "AiABKAsyJi5uYXJ1cGEucHJvdG9jb2wudG9wb2xvZ3kuVG9wb2xvZ3lEYXRh",
            "Ei0KCWRlbGltaXRlchgDIAEoDjIaLm5hcnVwYS5wcm90b2NvbC5EZWxpbWl0",
            "ZXJiBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Narupa.Protocol.Topology.TopologyReflection.Descriptor, global::Narupa.Protocol.DelimiterReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Narupa.Protocol.Instance.GetTopologyRequest), global::Narupa.Protocol.Instance.GetTopologyRequest.Parser, null, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Narupa.Protocol.Instance.GetTopologyResponse), global::Narupa.Protocol.Instance.GetTopologyResponse.Parser, new[]{ "FrameIndex", "Topology", "Delimiter" }, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GetTopologyRequest : pb::IMessage<GetTopologyRequest> {
    private static readonly pb::MessageParser<GetTopologyRequest> _parser = new pb::MessageParser<GetTopologyRequest>(() => new GetTopologyRequest());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<GetTopologyRequest> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Narupa.Protocol.Instance.GetTopologyReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetTopologyRequest() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetTopologyRequest(GetTopologyRequest other) : this() {
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetTopologyRequest Clone() {
      return new GetTopologyRequest(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as GetTopologyRequest);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(GetTopologyRequest other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(GetTopologyRequest other) {
      if (other == null) {
        return;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
        }
      }
    }

  }

  public sealed partial class GetTopologyResponse : pb::IMessage<GetTopologyResponse> {
    private static readonly pb::MessageParser<GetTopologyResponse> _parser = new pb::MessageParser<GetTopologyResponse>(() => new GetTopologyResponse());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<GetTopologyResponse> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Narupa.Protocol.Instance.GetTopologyReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetTopologyResponse() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetTopologyResponse(GetTopologyResponse other) : this() {
      frameIndex_ = other.frameIndex_;
      topology_ = other.topology_ != null ? other.topology_.Clone() : null;
      delimiter_ = other.delimiter_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public GetTopologyResponse Clone() {
      return new GetTopologyResponse(this);
    }

    /// <summary>Field number for the "frame_index" field.</summary>
    public const int FrameIndexFieldNumber = 1;
    private uint frameIndex_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint FrameIndex {
      get { return frameIndex_; }
      set {
        frameIndex_ = value;
      }
    }

    /// <summary>Field number for the "topology" field.</summary>
    public const int TopologyFieldNumber = 2;
    private global::Narupa.Protocol.Topology.TopologyData topology_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Narupa.Protocol.Topology.TopologyData Topology {
      get { return topology_; }
      set {
        topology_ = value;
      }
    }

    /// <summary>Field number for the "delimiter" field.</summary>
    public const int DelimiterFieldNumber = 3;
    private global::Narupa.Protocol.Delimiter delimiter_ = 0;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public global::Narupa.Protocol.Delimiter Delimiter {
      get { return delimiter_; }
      set {
        delimiter_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as GetTopologyResponse);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(GetTopologyResponse other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (FrameIndex != other.FrameIndex) return false;
      if (!object.Equals(Topology, other.Topology)) return false;
      if (Delimiter != other.Delimiter) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (FrameIndex != 0) hash ^= FrameIndex.GetHashCode();
      if (topology_ != null) hash ^= Topology.GetHashCode();
      if (Delimiter != 0) hash ^= Delimiter.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void WriteTo(pb::CodedOutputStream output) {
      if (FrameIndex != 0) {
        output.WriteRawTag(8);
        output.WriteUInt32(FrameIndex);
      }
      if (topology_ != null) {
        output.WriteRawTag(18);
        output.WriteMessage(Topology);
      }
      if (Delimiter != 0) {
        output.WriteRawTag(24);
        output.WriteEnum((int) Delimiter);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (FrameIndex != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(FrameIndex);
      }
      if (topology_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(Topology);
      }
      if (Delimiter != 0) {
        size += 1 + pb::CodedOutputStream.ComputeEnumSize((int) Delimiter);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(GetTopologyResponse other) {
      if (other == null) {
        return;
      }
      if (other.FrameIndex != 0) {
        FrameIndex = other.FrameIndex;
      }
      if (other.topology_ != null) {
        if (topology_ == null) {
          topology_ = new global::Narupa.Protocol.Topology.TopologyData();
        }
        Topology.MergeFrom(other.Topology);
      }
      if (other.Delimiter != 0) {
        Delimiter = other.Delimiter;
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(pb::CodedInputStream input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 8: {
            FrameIndex = input.ReadUInt32();
            break;
          }
          case 18: {
            if (topology_ == null) {
              topology_ = new global::Narupa.Protocol.Topology.TopologyData();
            }
            input.ReadMessage(topology_);
            break;
          }
          case 24: {
            delimiter_ = (global::Narupa.Protocol.Delimiter) input.ReadEnum();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code
