from io import StringIO
import os
import sys
import pytest

# Appending vm sibling directory to path because we can't change file structure
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../vm/")
from arrays import DataAllocator
from vm import VirtualMachine


def test_assemble_mem_overflow():
    ass = DataAllocator()
    program = [
        "hlt",
        ".data",
        "array: 1000"
    ]
    with pytest.raises(AssertionError):
        actual = ass.assemble(program)


def test_assemble_cumulative_mem_overflow():
    ass = DataAllocator()
    program = [
        "hlt",
        ".data",
        "array1: 200",
        "array2: 200"
    ]
    with pytest.raises(AssertionError):
        actual = ass.assemble(program)


def test_exe_mem_overflow():
    program = [
        "FF0102",  # ldc R1 255
        "FF0002",  # ldc R0 255
        "010006",  # add R0 R1, which is too high, 510
        "00000A",  # prr R0, 510
        "000105",  # str R1 R0, store R1 to address R0, which should be memory overlflow
        "000001"  # hlt
    ]
    program = [int(ln, 16) for ln in program]
    vm = VirtualMachine()
    vm.initialize(program)
    with pytest.raises(IndexError):
        vm.run()


def test_exe_unknown_instruction():
    program = [
        "FF0002",  # ldc R0 255
        "00000A",  # prr R0, 255
        "0101AA",  # unknown instruction!
        "000001"  # hlt
    ]
    program = [int(ln, 16) for ln in program]
    vm = VirtualMachine()
    vm.initialize(program)
    with pytest.raises(AssertionError):
        vm.run()


if __name__ == "__main__":
    pytest.main([os.path.basename(__file__)])
