from telemetry_f1_2021.listener import TelemetryListener
import socket
from packets import Header
import ctypes


def read_from_json():
    pass


class Lpm(ctypes.LittleEndianStructure):

    @classmethod
    def unpack(cls, buffer):
        return cls.from_buffer_copy(buffer)


def main():
    listener = TelemetryListener(port=20777, host='')
    # udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    # udp_socket.bind(('', 20777))
    try:
        #  while True:
        #   packet = udp_socket.recv(2048)
        #   header = Header.from_buffer_copy(packet)
        #   print(packet)
        obj = Lpm()
        print(obj.unpack(
            b'\xe5\x07\x01\x12\x01\x03\xc3lVn\xe8)\xf6N\x1eG&B\x9a\x07\x00\x00\x00\xffBUTN\x00\x00\x00\x00\xd3\x01\x00\x00'
            ))
        ## if header.m_packet_id == 7:
        ##    print("do nothing")
        #  for data in header.m_header.
        # ver una forma de no armar una tupla con la info, se podra?
    except KeyboardInterrupt:
        print('Stop the car, stop the car Checo.')
        print('Stop the car, stop at pit exit.')
        print('Just pull over to the side.')


if __name__ == "__main__":
    main()
