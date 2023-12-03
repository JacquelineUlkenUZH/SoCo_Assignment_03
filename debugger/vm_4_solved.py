import sys
import inspect

from architecture import OPS, VMState
from vm_break import VirtualMachineBreak

# Class hierarchy: base > step > extended > break > 4solved
class VirtualMachine4solved(VirtualMachineBreak):

    # [interact]
    def interact(self, addr):
        prompt = "".join(sorted({key[0] for key in self.handlers}))
        interacting = True
        while interacting:
            try:
                command, *cargs = self.read(f"{addr:06x} [{prompt}]> ").split(" ")
                if not command:
                    continue
                elif command not in self.handlers:
                    self.write(f"Unknown command {command}")
                # Functions with 2 arguments (self, addr) from "old" parent classes
                elif len(inspect.signature(self.handlers[command]).parameters) == 1:
                    interacting = self.handlers[command](self.ip)
                # New functions with 3+ arguments (self, addr, *cargs)
                else:
                    interacting = self.handlers[command](self.ip, *cargs)
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
    # [/interact]
    
    def show_memory(self, start, end=None):
        if end is None: end = start # note end+1 in range()
        if start > end: start, end = end, start
        if not (0 <= start < len(self.ram) and end < len(self.ram)):
            self.write(f"Invalid memory address")
            return True
        for addr in range(start, end+1):
            self.write(f"{addr:06x}: {self.ram[addr]:06x}")

    # [memory]
    def _do_memory(self, addr, *cargs):
        if len(cargs) == 0: self.show()
        if len(cargs) == 1: self.show_memory(int(cargs[0]))
        if len(cargs) == 2: self.show_memory(int(cargs[0]), int(cargs[1]))
        
        return True
    # [/memory]
    

if __name__ == "__main__":
    VirtualMachine4solved.main()

