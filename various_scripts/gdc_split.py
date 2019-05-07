# A script that was used to help debug issues with decoding the GameDataClient protobuf due
# to terribly vague error messages
import binascii
from WUProtos.Data.Client import ClientGmTemplate_pb2
from google.protobuf.json_format import MessageToJson

f = open('GameDataClient.bytes', 'rb')
s = f.read()
f.close()

# Returns a tuple of the result and number of bytes read
def read_varint(stream):
    pos = 0
    shift = 0
    res = 0
    while True:
        i = stream[pos]
        res |= (i & 0x7f) << shift
        shift += 7
        pos += 1
        if i >> 7 == 0:
            break
    return (res, pos)

# returns a tuple with the field number, the wire type, and how many bytes were read
def get_field_wire(stream):
    wire_type = stream[0] & 0x07 # bottom 3 bits are wire type
    first = True
    shift = 0
    pos = 0
    field_num = 0
    while True:
        i = stream[pos]
        if first:
            field_num = (i >> 3) & 0xF
            shift += 4
        else:
            field_num |= (i & 0x7f) << shift
            shift += 7
        pos += 1
        if i >> 7 == 0:
            break

    return (field_num, wire_type, pos)

print(binascii.hexlify(s[0:3]))
pos = 0
while(pos < len(s)):
    (field_num, wire_type, i) = get_field_wire(s[pos:])
    if wire_type != 2 and field_num != 1:
        print('Error: Invalid wire_type (%d) or unexpected field_num (%d)' % (wire_type, field_num))
        exit()
    pos += i
    length, i = read_varint(s[pos:])
    end = pos + i + length

    pos += i # skip the varint bytes
    proto_chunk = s[pos:pos + length]
    print(binascii.hexlify(proto_chunk))

    wrapper = ClientGmTemplate_pb2.ClientGmTemplate()
    wrapper.ParseFromString(proto_chunk)
    print(MessageToJson(wrapper))



    pos = end
    #print(length)
