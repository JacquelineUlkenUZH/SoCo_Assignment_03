import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../vm/")
from assembler import Assembler


def test_count_up():
    with open("count_up.as", "r") as file:
        ass = Assembler()
        count_up_hex = ass.assemble(file.readlines())
        with open("count_up.mx", "r") as mx:
            assert mx.read().splitlines() == count_up_hex


def test_memory():
    with open("memory.as", "r") as file:
        ass = Assembler()
        memory_hex = ass.assemble(file.readlines())
        with open("memory.mx", "r") as mx:
            assert mx.read().splitlines() == memory_hex
