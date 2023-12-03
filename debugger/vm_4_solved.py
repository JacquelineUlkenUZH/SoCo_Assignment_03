import sys
import inspect

from architecture import OPS, VMState
from vm_break import VirtualMachineBreak

# Class hierarchy: base > step > extended > break > 4solved
class VirtualMachine4solved(VirtualMachineBreak):
    
    def __init__(self):
        super().__init__()
        
        # Adding abbreviations for commands while avoiding duplicates
        duplicates = []
        for cmd in list(self.handlers.keys()):
            for end in range(1, len(cmd)):
                if cmd[:end] in self.handlers:
                    duplicates.append(cmd[:end])
                else:
                    self.handlers[cmd[:end]] = self.handlers[cmd]
        for cmd in duplicates:
            del self.handlers[cmd]
                

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
                # to keep old functionality, as in the book
                elif len(inspect.signature(self.handlers[command]).parameters) == 1:
                    interacting = self.handlers[command](self.ip)
                # New functions with 3+ arguments (self, addr, *cargs)
                else:
                    valid_cargs, cargs = self._cargs_to_addresses(cargs)
                    if valid_cargs:
                        interacting = self.handlers[command](self.ip, *cargs)
                    else:
                        self.write(f"Invalid memory address")
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False
    # [/interact]
    
    def _cargs_to_addresses(self, cargs):
        """Checks if arguments are valid memory addresses and returns them as sorted list of integers.

        Args:
            cargs (str[]): List of strings representing memory addresses

        Returns:
            bool: True if all arguments are valid memory addresses
            int[]: Sorted list of integers representing memory addresses
        """         
        for i, arg in enumerate(cargs):
            if not arg.isdigit():
                return False, []
            cargs[i] = int(arg)
            if not (0 <= cargs[i] < len(self.ram)):
                return False, []
        if len(cargs) >= 2 and cargs[0] == cargs[1]:
            return False, []
        return True, sorted(cargs)
    
    # [memory]
    def _do_memory(self, addr, *cargs):
        if len(cargs) == 0: self.show()
        else:
            start = cargs[0]
            end = cargs[1] if len(cargs) > 1 else start
            
            for addr in range(start, end+1):
                self.write(f"{addr:06x}: {self.ram[addr]:06x}")
        
        return True
    # [/memory]
    

    # [add]
    def _do_add_breakpoint(self, addr, *cargs):
        if cargs: addr = cargs[0]
        return super()._do_add_breakpoint(addr)
    # [/add]

    # [clear]
    def _do_clear_breakpoint(self, addr, *cargs):
        if cargs: addr = cargs[0]
        return super()._do_clear_breakpoint(addr)
    # [/clear]

if __name__ == "__main__":
    VirtualMachine4solved.main()

