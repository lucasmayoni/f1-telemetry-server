from telemetry_f1_2021.listener import TelemetryListener
import socket
import ctypes


def read_from_json():
    pass


class Header(ctypes.LittleEndianStructure):
    _fields_ = [
        ('m_packet_format', ctypes.c_uint16),  # 2021
        ('m_game_major_version', ctypes.c_uint8),  # Game major version - "X.00"
        ('m_game_minor_version', ctypes.c_uint8),  # Game minor version - "1.XX"
        ('m_packet_version', ctypes.c_uint8),  # Version of this packet type, all start from 1
        ('m_packet_id', ctypes.c_uint8),  # Identifier for the packet type, see below
        ('m_session_uid', ctypes.c_uint64),  # Unique identifier for the session
        ('m_session_time', ctypes.c_float),  # Session timestamp
        ('m_frame_identifier', ctypes.c_uint32),  # Identifier for the frame the data was retrieved on
        ('m_player_car_index', ctypes.c_uint8),  # Index of player's car in the array
        ('m_secondary_player_car_index', ctypes.c_uint8),  # Index of secondary player's car in the array (splitscreen)
        # 255 if no second player
    ]

    def to_dict(self):
        """Returns a ``dict`` with key-values derived from _fields_"""
        return {k: self.get_value(k) for k, _ in self._fields_}

    def to_json(self):
        """Returns a ``str`` of sorted JSON derived from _fields_"""
        return self.to_dict()

    def __repr__(self):
        return self.to_json()


def main():
    # listener = TelemetryListener(port=20777, host='')
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_socket.bind(('', 20777))
    try:
        while True:
            packet = udp_socket.recv(2048)
            header = Header.from_buffer_copy(packet)
            print("RPM: %s", header)
    except KeyboardInterrupt:
        print('Stop the car, stop the car Checo.')
        print('Stop the car, stop at pit exit.')
        print('Just pull over to the side.')


if __name__ == "__main__":
    main()
