// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: narupa/protocol/topology/ChainInfo.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Narupa.Protocol.Topology {

  /// <summary>Holder for reflection information generated from narupa/protocol/topology/ChainInfo.proto</summary>
  public static partial class ChainInfoReflection {

    #region Descriptor
    /// <summary>File descriptor for narupa/protocol/topology/ChainInfo.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static ChainInfoReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CihuYXJ1cGEvcHJvdG9jb2wvdG9wb2xvZ3kvQ2hhaW5JbmZvLnByb3RvEhhu",
            "YXJ1cGEucHJvdG9jb2wudG9wb2xvZ3kiLgoJQ2hhaW5JbmZvEhMKC2NoYWlu",
            "X2luZGV4GAEgASgNEgwKBG5hbWUYAyABKAliBnByb3RvMw=="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Narupa.Protocol.Topology.ChainInfo), global::Narupa.Protocol.Topology.ChainInfo.Parser, new[]{ "ChainIndex", "Name" }, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class ChainInfo : pb::IMessage<ChainInfo> {
    private static readonly pb::MessageParser<ChainInfo> _parser = new pb::MessageParser<ChainInfo>(() => new ChainInfo());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pb::MessageParser<ChainInfo> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Narupa.Protocol.Topology.ChainInfoReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ChainInfo() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ChainInfo(ChainInfo other) : this() {
      chainIndex_ = other.chainIndex_;
      name_ = other.name_;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public ChainInfo Clone() {
      return new ChainInfo(this);
    }

    /// <summary>Field number for the "chain_index" field.</summary>
    public const int ChainIndexFieldNumber = 1;
    private uint chainIndex_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public uint ChainIndex {
      get { return chainIndex_; }
      set {
        chainIndex_ = value;
      }
    }

    /// <summary>Field number for the "name" field.</summary>
    public const int NameFieldNumber = 3;
    private string name_ = "";
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public string Name {
      get { return name_; }
      set {
        name_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override bool Equals(object other) {
      return Equals(other as ChainInfo);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public bool Equals(ChainInfo other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (ChainIndex != other.ChainIndex) return false;
      if (Name != other.Name) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public override int GetHashCode() {
      int hash = 1;
      if (ChainIndex != 0) hash ^= ChainIndex.GetHashCode();
      if (Name.Length != 0) hash ^= Name.GetHashCode();
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
      if (ChainIndex != 0) {
        output.WriteRawTag(8);
        output.WriteUInt32(ChainIndex);
      }
      if (Name.Length != 0) {
        output.WriteRawTag(26);
        output.WriteString(Name);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public int CalculateSize() {
      int size = 0;
      if (ChainIndex != 0) {
        size += 1 + pb::CodedOutputStream.ComputeUInt32Size(ChainIndex);
      }
      if (Name.Length != 0) {
        size += 1 + pb::CodedOutputStream.ComputeStringSize(Name);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    public void MergeFrom(ChainInfo other) {
      if (other == null) {
        return;
      }
      if (other.ChainIndex != 0) {
        ChainIndex = other.ChainIndex;
      }
      if (other.Name.Length != 0) {
        Name = other.Name;
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
            ChainIndex = input.ReadUInt32();
            break;
          }
          case 26: {
            Name = input.ReadString();
            break;
          }
        }
      }
    }

  }

  #endregion

}

#endregion Designer generated code
