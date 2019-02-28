// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: narupa/protocol/trajectory/LoadTrajectory.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Narupa.Protocol.Trajectory {

  /// <summary>Holder for reflection information generated from narupa/protocol/trajectory/LoadTrajectory.proto</summary>
  public static partial class LoadTrajectoryReflection {

    #region Descriptor
    /// <summary>File descriptor for narupa/protocol/trajectory/LoadTrajectory.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static LoadTrajectoryReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "Ci9uYXJ1cGEvcHJvdG9jb2wvdHJhamVjdG9yeS9Mb2FkVHJhamVjdG9yeS5w",
            "cm90bxIabmFydXBhLnByb3RvY29sLnRyYWplY3RvcnkiOgoVTG9hZFRyYWpl",
            "Y3RvcnlSZXF1ZXN0EgwKBHBhdGgYASABKAkSEwoLaW5zdGFuY2VfaWQYAiAB",
            "KAkiLQoWTG9hZFRyYWplY3RvcnlSZXNwb25zZRITCgtpbnN0YW5jZV9pZBgB",
            "IAEoCWIGcHJvdG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Narupa.Protocol.Trajectory.LoadTrajectoryRequest), global::Narupa.Protocol.Trajectory.LoadTrajectoryRequest.Parser, new[]{ "Path", "InstanceId" }, null, null, null),
            new pbr::GeneratedClrTypeInfo(typeof(global::Narupa.Protocol.Trajectory.LoadTrajectoryResponse), global::Narupa.Protocol.Trajectory.LoadTrajectoryResponse.Parser, new[]{ "InstanceId" }, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class LoadTrajectoryRequest : pb::IMessage<LoadTrajectoryRequest> {
    private static readonly pb::MessageParser<LoadTrajectoryRequest> _parser = new pb::MessageParser<LoadTrajectoryRequest>(() => new LoadTrajectoryRequest());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<LoadTrajectoryRequest> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Narupa.Protocol.Trajectory.LoadTrajectoryReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LoadTrajectoryRequest() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LoadTrajectoryRequest(LoadTrajectoryRequest other) : this() {
      path_ = other.path_;
      instanceId_ = other.instanceId_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LoadTrajectoryRequest Clone() {
      return new LoadTrajectoryRequest(this);
    }

    /// <summary>Field number for the "path" field.</summary>
    public const int PathFieldNumber = 1;
    private string path_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Path {
      get { return path_; }
      set {
        path_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    /// <summary>Field number for the "instance_id" field.</summary>
    public const int InstanceIdFieldNumber = 2;
    private string instanceId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string InstanceId {
      get { return instanceId_; }
      set {
        instanceId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as LoadTrajectoryRequest);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(LoadTrajectoryRequest other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (Path != other.Path) return false;
      if (InstanceId != other.InstanceId) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (Path.Length != 0) hash ^= Path.GetHashCode();
      if (InstanceId.Length != 0) hash ^= InstanceId.GetHashCode();
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
      if (Path.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(Path);
      }
      if (InstanceId.Length != 0) {
        output.WriteRawTag(18);
        output.WriteString(InstanceId);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (Path.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Path);
      }
      if (InstanceId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(InstanceId);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(LoadTrajectoryRequest other) {
      if (other == null) {
        return;
      }
      if (other.Path.Length != 0) {
        Path = other.Path;
      }
      if (other.InstanceId.Length != 0) {
        InstanceId = other.InstanceId;
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
          case 10: {
            Path = input.ReadString();
            break;
          }
          case 18: {
            InstanceId = input.ReadString();
            break;
          }
        }
      }
    }

  }

  public sealed partial class LoadTrajectoryResponse : pb::IMessage<LoadTrajectoryResponse> {
    private static readonly pb::MessageParser<LoadTrajectoryResponse> _parser = new pb::MessageParser<LoadTrajectoryResponse>(() => new LoadTrajectoryResponse());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<LoadTrajectoryResponse> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Narupa.Protocol.Trajectory.LoadTrajectoryReflection.Descriptor.MessageTypes[1]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LoadTrajectoryResponse() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LoadTrajectoryResponse(LoadTrajectoryResponse other) : this() {
      instanceId_ = other.instanceId_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public LoadTrajectoryResponse Clone() {
      return new LoadTrajectoryResponse(this);
    }

    /// <summary>Field number for the "instance_id" field.</summary>
    public const int InstanceIdFieldNumber = 1;
    private string instanceId_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string InstanceId {
      get { return instanceId_; }
      set {
        instanceId_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as LoadTrajectoryResponse);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(LoadTrajectoryResponse other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (InstanceId != other.InstanceId) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (InstanceId.Length != 0) hash ^= InstanceId.GetHashCode();
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
      if (InstanceId.Length != 0) {
        output.WriteRawTag(10);
        output.WriteString(InstanceId);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (InstanceId.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(InstanceId);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(LoadTrajectoryResponse other) {
      if (other == null) {
        return;
      }
      if (other.InstanceId.Length != 0) {
        InstanceId = other.InstanceId;
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
          case 10: {
            InstanceId = input.ReadString();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code
