from io import StringIO
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../vm/")
from vm import VirtualMachine


def test_vm_count_up():
    with open("count_up.mx", "r") as file:
        vm_1 = VirtualMachine()
        lines = [ln.strip() for ln in file.readlines()]
        program = [int(ln, 16) for ln in lines if ln]
        vm_1.initialize(program)
        captured_output = StringIO()
        sys.stdout = captured_output
        vm_1.run()
        sys.stdout = sys.__stdout__
        with open("run_count_up", "r") as run_count_up:
            print(run_count_up.read())
            print(captured_output.getvalue())
            assert captured_output.getvalue() == run_count_up.read()
        writer = open("vm_output_count_up", "w")
        vm_1.show(writer)
        with open("show_count_up", "r") as show_count_up:
            with open("vm_output", "r") as vm_output_count_up:
                print(show_count_up.read())
                print(vm_output_count_up.read())
                print("------------------")
                assert show_count_up.read() == vm_output_count_up.read()


def test_vm_memory():
    with open("memory.mx", "r") as file:
        vm_2 = VirtualMachine()
        lines = [ln.strip() for ln in file.readlines()]
        program = [int(ln, 16) for ln in lines if ln]
        vm_2.initialize(program)
        captured_output = StringIO()
        sys.stdout = captured_output
        vm_2.run()
        sys.stdout = sys.__stdout__
        with open("run_memory", "r") as run_memory:
            print(run_memory.read())
            print(captured_output.getvalue())
            assert captured_output.getvalue() == run_memory.read() # check if read is correct (maybe read the file as one string)
        writer = open("vm_output_memory", "w")
        vm_2.show(writer)
        with open("show_memory", "r") as show_memory:
            with open("vm_output_memory", "r") as vm_output_memory:
                print(show_memory.read())
                print(vm_output_memory.read())
                assert show_memory.read() == vm_output_memory.read()


def main():
    test_vm_count_up()
    test_vm_memory()


if __name__ == "__main__":
    main()


# def test_count_up():
#     with open("count_up.as", "r") as file:
#         ass = Assembler()
#         count_up_hex = ass.assemble(file.readlines())
#         with open("count_up.mx", "r") as mx:
#             assert mx.read().splitlines() == count_up_hex
#
#
# def test_memory():
#     with open("memory.as", "r") as file:
#         ass = Assembler()
#         memory_hex = ass.assemble(file.readlines())
#         with open("memory.mx", "r") as mx:
#             assert mx.read().splitlines() == memory_hex
