from dataclasses import dataclass, field

@dataclass
class RAM:
    # creates a unique 2,048 byte array every time new obj is instantiated, don't include in __init__
    _data: bytearray = field(default_factory = lambda: bytearray(0x800), init = False) # storage contains 0x800 bytes

    # changes byte read from same physical address
    def write(self, addr: int, value: int) -> None:
        self._data[addr] = value

    # takes addr and returns byte stored at index
    def read(self, addr: int) -> int:
        return self._data[addr]