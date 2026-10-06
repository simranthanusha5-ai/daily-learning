"""Day 143: Python Bytecode Disassembly."""
import dis

def calculate(x, y):
    return (x + y) * 2

def inspect_opcodes(func):
    instructions = list(dis.get_instructions(func))
    opnames = [instr.opname for instr in instructions]
    return opnames

if __name__ == "__main__":
    opcodes = inspect_opcodes(calculate)
    assert "BINARY_OP" in opcodes or "BINARY_ADD" in opcodes or "RETURN_VALUE" in opcodes
    print("Day 143 Bytecode Inspection tests passed!")
