import os
import sys
from io import StringIO

# Appending vm sibling directory to path because we can't change file structure
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../vm/")
from assembler import Assembler
from vm import VirtualMachine
from arrays import DataAllocator

def test_3_1():
    
    expected_output = """
>> 3
>> 2
>> 1
>> 0
>> 1
>> 2
>> 3
"""
    expected_output = expected_output[1:] # Strip first newline because it's more readable that way
    
    # Assembling
    ass = Assembler()
    with open("example_3_1.as", "r") as file:
        actual_program = ass.assemble(file.readlines())
    actual_program = [int(ln.strip(), 16) for ln in actual_program if ln]

    # Setup VM
    vm = VirtualMachine()
    vm.initialize(actual_program)
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Running
    try:
        vm.run()
    
    # Teardown no matter what happens
    finally:
        actual_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
    
    assert actual_output == expected_output

def test_3_2():
    
    expected_output = """
>> 3
>> 7
>> 7
>> 3
"""
    expected_output = expected_output[1:] # Strip first newline because it's more readable that way
    
    # Assembling
    ass = Assembler()
    with open("example_3_2.as", "r") as file:
        actual_program = ass.assemble(file.readlines())
    actual_program = [int(ln.strip(), 16) for ln in actual_program if ln]

    # Setup VM
    vm = VirtualMachine()
    vm.initialize(actual_program)
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Running
    try:
        vm.run()
    
    # Teardown no matter what happens
    finally:
        actual_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
    
    assert actual_output == expected_output

def test_3_3():
    
    expected_output = """
>> 1
>> 1
>> 2
>> 3
>> 5
>> 8
>> 13
>> 21
>> 34
>> 55
>> 55
>> 34
>> 21
>> 13
>> 8
>> 5
>> 3
>> 2
>> 1
>> 1
"""
    expected_output = expected_output[1:] # Strip first newline because it's more readable that way
    
    # Assembling
    ass = DataAllocator()
    with open("example_3_3.as", "r") as file:
        actual_program = ass.assemble(file.readlines())
    actual_program = [int(ln.strip(), 16) for ln in actual_program if ln]

    # Setup VM
    vm = VirtualMachine()
    vm.initialize(actual_program)
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Running
    try:
        vm.run()
    
    # Teardown no matter what happens
    finally:
        actual_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
    
    assert actual_output == expected_output

if __name__ == "__main__":
    import pytest
    pytest.main([os.path.basename(__file__)])
