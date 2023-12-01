import os
import sys

# Appending vm sibling directory to path because we can't change file structure
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/../vm/")
from architecture import NUM_REG, OP_SHIFT, OPS

# [class]
class Disassembler:
    def __init__(self):
        # Reverse the OPS dictionary for quick lookup
        self.revOPS = {v["code"]: k for k, v in OPS.items()}
        
    def disassemble(self, lines):
        lines = self._get_lines(lines)
        decompiled = [self._decompile(instr) for instr in lines]
        return decompiled
# [/class]

    # [compile]
    def _decompile(self, instruction):
        opnr, *args = int(instruction[4:6], 16), instruction[2:4], instruction[0:2]
        op = self.revOPS[opnr]
        fmt = OPS[op]["fmt"]

        if fmt == "--":
            return f"{op}"

        elif fmt == "r-":
            return f"{op} R{self._reg(args[0])}"

        elif fmt == "rr":
            return f"{op} R{self._reg(args[0])} R{self._reg(args[1])}"

        elif fmt == "rv":
            return f"{op} R{self._reg(args[0])} {int(args[1], 16)}"
    # [/compile]

    def _get_lines(self, lines):
        lines = [ln.strip() for ln in lines]
        lines = [ln for ln in lines if len(ln) > 0]
        return lines

    def _reg(self, token):
        r = int(token)
        assert 0 <= r < NUM_REG, f"Illegal register {token}"
        return r

def main(disassembler_cls):
    assert len(sys.argv) == 3, f"Usage: {sys.argv[0]} input|- output|-"
    reader = open(sys.argv[1], "r") if (sys.argv[1] != "-") else sys.stdin
    writer = open(sys.argv[2], "w") if (sys.argv[2] != "-") else sys.stdout
    
    lines = reader.readlines()
    disassembler = disassembler_cls()
    program = disassembler.disassemble(lines)
    for instruction in program:
        print(instruction, file=writer)

if __name__ == "__main__":
    main(Disassembler)
