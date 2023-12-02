from io import StringIO
import os
import sys
import pytest

# Appending vm sibling directory to path because we can't change file structure
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../vm/")
from arrays import DataAllocator
from vm import VirtualMachine

def negative_show():
    ass = DataAllocator()
    program = [
        "ldc R1 50",
        "sub R0 R1",
        "str R0 R1",
        "prr R0",
        "prm R1",
        "ldc R2 55",
        "add R0 R2",
        "prr R0",
        "ldr R3 R1",
        "add R3 R2",
        "str R3 R1",
        "prm R1",
        "hlt"
    ]

    program = ass.assemble(program)
        
    program = [int(ln, 16) for ln in program]
    vm = VirtualMachine()
    vm.initialize(program)
    vm.run()


if __name__ == "__main__":
    negative_show()
