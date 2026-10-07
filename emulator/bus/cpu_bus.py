from dataclasses import dataclass, field
from emulator.memory.ram import RAM

@dataclass
class CpuBus:
    # initialize system memory
    ram: RAM = field(default_factory = RAM)

    def read(self, addr: int) -> int:
        # 8 KB range for CPU to request addresses, but NES only works with 2KB of memory, so memory mirrors itself over
        # the range 4 times.
        if 0x0000 <= addr <= 0x1FFF:
            return self.ram.read(addr & 0x07FF) # force address to wrap around and point to correct 2KB address

        # prevents CPU from reading outside range
        raise ValueError(f"unsupported CPU bus read: {addr:04X}")

    def write(self, addr: int, value: int) -> None:
        if 0x0000 <= addr <= 0x1FFF:
            self.ram.write(addr & 0x07FF, value)
            return

        raise ValueError(f"unsupported CPU bus write: {addr:04X}")