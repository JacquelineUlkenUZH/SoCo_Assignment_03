from io import StringIO
import os
import sys

# Appending vm sibling directory to path because we can't change file structure
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../vm/")
from vm import VirtualMachine


def test_vm_count_up():
    # Setup
    with open("count_up.mx", "r") as file:
        lines = [ln.strip() for ln in file.readlines()]
    program = [int(ln.split("#")[0].strip(), 16) for ln in lines if ln]  # Strip comments if using manual .mx files
    vm = VirtualMachine()
    vm.initialize(program)
    captured_output = StringIO()
    sys.stdout = captured_output

    # Running
    try:
        vm.run()

    # Teardown no matter what happens
    finally:
        actual = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    # Comparisons
    with open("count_up_expected_out.log", "r") as file:
        expected = file.read()
    assert actual == expected


def test_vm_memory():
    with open("memory.mx", "r") as file:
        lines = [ln.strip() for ln in file.readlines()]
    program = [int(ln.split("#")[0].strip(), 16) for ln in lines if ln]  # Strip comments if using manual .mx files
    vm = VirtualMachine()
    vm.initialize(program)
    captured_output = StringIO()
    sys.stdout = captured_output

    # Running
    try:
        vm.run()

    # Teardown no matter what happens
    finally:
        actual = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    # Comparisons
    with open("memory_expected_out.log", "r") as file:
        expected = file.read()
    assert actual == expected


def test_simple_arithmetic():
    with open("simple_arithmetic.mx", "r") as file:
        lines = [ln.strip() for ln in file.readlines()]
    program = [int(ln.split("#")[0].strip(), 16) for ln in lines if ln]  # Strip comments if using manual .mx files
    vm = VirtualMachine()
    vm.initialize(program)
    captured_output = StringIO()
    sys.stdout = captured_output

    # Running
    try:
        vm.run()

    # Teardown no matter what happens
    finally:
        actual = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    # Comparisons
    with open("simple_arithmetic_expected_out.log", "r") as file:
        expected = file.read()
    assert actual == expected


if __name__ == "__main__":
    import pytest

    pytest.main([os.path.basename(__file__)])
