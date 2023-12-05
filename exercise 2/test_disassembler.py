import os
import sys

from disassemble import Disassembler
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def test_simplearithmetic():
    ass = Disassembler()
    #disassembling
    with open("simple_arithmetic.mx", "r") as file:
        actual = ass.disassemble(file.readlines())
    # Testing against manual solution stripped of comments and empty lines
    with open("simple_arithmetic_expected.as", "r") as mx:
        expected = [l for l in mx.read().splitlines() if l and not l.startswith("#")]
        
    assert actual == expected

def test_memory():
    ass = Disassembler()
    #disassembling
    with open("input_file.mx", "r") as file:
        actual = ass.disassemble(file.readlines())
    # Testing against manual solution stripped of comments and empty lines
    with open("output_file_expected.as", "r") as mx:
        expected = [l for l in mx.read().splitlines() if l and not l.startswith("#")]
        
    assert actual == expected

def test_count_up():
    ass = Disassembler()
    #disassembling
    with open("count_up.mx", "r") as file:
        actual = ass.disassemble(file.readlines())
    # Testing against manual solution stripped of comments and empty lines
    with open("count_up_expected.as", "r") as mx:
        expected = [l for l in mx.read().splitlines() if l and not l.startswith("#")]
        
    assert actual == expected

if __name__ == "__main__":
    import pytest
    pytest.main([os.path.basename(__file__)])