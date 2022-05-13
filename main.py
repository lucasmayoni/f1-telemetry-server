from telemetry_f1_2021.listener import TelemetryListener
import socket
from packets import Header


def read_from_json():
    pass


def main():
    # listener = TelemetryListener(port=20777, host='')
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_socket.bind(('', 20777))
    try:
        while True:
            packet = udp_socket.recv(2048)
            header = Header.from_buffer_copy(packet)
            if header.m_packet_id == 7:
                #  for data in header.m_header.
                # ver una forma de no armar una tupla con la info, se podra?
    except KeyboardInterrupt:
        print('Stop the car, stop the car Checo.')
        print('Stop the car, stop at pit exit.')
        print('Just pull over to the side.')


if __name__ == "__main__":
    main()
