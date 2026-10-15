from dataclasses import dataclass

from emulator.bus.cpu_bus import CpuBus

@dataclass
# MOS 6502
class CPU:
    bus: CpuBus
    a: int = 0 # accumulator
    x: int = 0 # index register 1
    y: int = 0 # index register 2
    pc: int = 0 # program counter
    s: int = 0 # stack pointer
    p: int = 0 # processor status

    # reads single byte from memory at curr pc location
    def fetch_byte(self) -> int:
        value = self.bus.read(self.pc)
        self.pc += 1
        return value

    # reads two bytes from memory (full address)
    def fetch_word(self) -> int:
        low = self.fetch_byte()
        high = self.fetch_byte()
        return low | (high << 8) # merge low byte into empty zeroes created by 8-bit high shift for full 16-bit return