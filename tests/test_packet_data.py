from packets import Header


def test_packet_header():
    """Test version 1.09 packet header"""

    data = b"\xe4\x07\x01\t\x01\x03\xa3\x80\x9atC\xc0\x8e}:\x11\tD\xab\\\x00\x00\xff\xffPENA\x05\x07\x04\xff\xff\x05\x00"
    header = Header.from_buffer_copy(data)
    assert header.m_packetFormat == 2020
    assert header.m_gameMajorVersion == 1
    assert header.m_gameMinorVersion == 9

