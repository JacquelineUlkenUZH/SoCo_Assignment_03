import os
import sys

# Appending vm sibling directory to path because we can't change file structure
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../vm/")
from assembler import Assembler


def test_simplearithmetic():
    ass = Assembler()
    with open("simple_arithmetic.as", "r") as file:
        actual = ass.assemble(file.readlines())
    with open("simple_arithmetic.mx", "w") as file:
        for l in actual:
            print(l, file=file)
    # Testing against manual solution stripped of comments
    with open("simple_arithmetic_expected.mx", "r") as mx:
        expected = mx.read().splitlines()
        for i, line in enumerate(expected):
            expected[i] = line.split("#")[0].strip()
    assert actual == expected


def test_count_up():
    ass = Assembler()
    with open("count_up.as", "r") as file:
        actual = ass.assemble(file.readlines())
    with open("count_up.mx", "w") as file:
        for l in actual:
            print(l, file=file)
    # Testing against manual solution
    with open("count_up_expected.mx", "r") as mx:
        expected = mx.read().splitlines()
        for i, line in enumerate(expected):
            expected[i] = line.split("#")[0].strip()
    assert actual == expected


def test_memory():
    ass = Assembler()
    with open("memory.as", "r") as file:
        actual = ass.assemble(file.readlines())
    with open("memory.mx", "w") as file:
        for l in actual:
            print(l, file=file)
    # Testing against manual solution
    with open("memory_expected.mx", "r") as mx:
        expected = mx.read().splitlines()
        for i, line in enumerate(expected):
            expected[i] = line.split("#")[0].strip()
    assert actual == expected
