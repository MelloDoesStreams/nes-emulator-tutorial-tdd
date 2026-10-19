from dataclasses import dataclass, field
from typing import Optional

from emulator.memory.ram import RAM
from emulator.memory.memory_device import MemoryDevice

@dataclass
class CpuBus:
    # initialize ROM, bus can still be initialized without ROM loaded
    program_rom: Optional[MemoryDevice] = None
    # initialize system memory
    ram: RAM = field(default_factory = RAM)

    def read(self, addr: int) -> int:
        # 8 KB range for CPU to request addresses, but NES only works with 2KB of memory, so memory mirrors itself over
        # the range 4 times.
        if 0x0000 <= addr <= 0x1FFF:
            return self.ram.read(addr & 0x07FF) # force address to wrap around and point to correct 2KB address

        if 0x8000 <= addr <= 0xFFFF: # ROM addr range
            # ROM must be loaded before reading
            if self.program_rom is None:
                raise ValueError("no program ROM attached")

            return self.program_rom.read(addr - 0x8000) # translate memory into zero-based local index

        # prevents CPU from reading outside range
        raise ValueError(f"unsupported CPU bus read: {addr:04X}")

    def write(self, addr: int, value: int) -> None:
        if 0x0000 <= addr <= 0x1FFF:
            self.ram.write(addr & 0x07FF, value)
            return

        raise ValueError(f"unsupported CPU bus write: {addr:04X}")