import ctypes


class AbstractPacket(ctypes.LittleEndianStructure):

    @classmethod
    def size(cls):
        return ctypes.sizeof(cls)

    @classmethod
    def unpack(cls, buffer):
        return cls.from_buffer_copy(buffer)

    def __repr__(self) -> str:
        return '{self.__class__.__name__}({self.m_packetFormat},' \
               '{self.m_packetVersion},' \
               '{self.m_sessionUID})'.format(self=self)


class Header(AbstractPacket):
    _fields_ = [
        ("m_packetFormat", ctypes.c_uint16),
        ("m_gameMajorVersion", ctypes.c_uint8),
        ("m_gameMinorVersion", ctypes.c_uint8),
        ("m_packetVersion", ctypes.c_uint8),
        ("m_packetId", ctypes.c_uint8),
        ("m_sessionUID", ctypes.c_uint64),
        ("m_sessionTime", ctypes.c_float),
        ("m_frameIdentifier", ctypes.c_uint32),
        ("m_playerCardIndex", ctypes.c_uint8),
        ("m_secondaryPlayerCardIndex", ctypes.c_uint8)
    ]