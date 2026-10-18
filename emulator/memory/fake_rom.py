from dataclasses import dataclass, field
from emulator.memory.memory_device import MemoryDevice

@dataclass
class FakeROM(MemoryDevice):
    # 32 KB RAM
    _data: bytearray = field(default_factory = lambda: bytearray(0x8000), init = False)

    def write(self, addr: int, value: int) -> None:
        self._data[addr] = value

    def read(self, addr: int) -> int:
        return self._data[addr]