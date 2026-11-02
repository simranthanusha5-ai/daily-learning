"""Day 372: Mini eBPF Bytecode Verifier."""

class EBPFVerifier:
    @staticmethod
    def verify(instructions):
        # Prevent backward loops and ensure termination
        for i, ins in enumerate(instructions):
            op, target = ins
            if op == "JMP" and target <= i:
                raise ValueError("eBPF Verifier Error: Backwards loop detected")
        return True

class MiniEBPFVM:
    def __init__(self):
        self.registers = [0] * 11

    def run(self, program):
        EBPFVerifier.verify(program)
        for op, arg in program:
            if op == "MOV": self.registers[0] = arg
            elif op == "ADD": self.registers[0] += arg
        return self.registers[0]

if __name__ == "__main__":
    vm = MiniEBPFVM()
    prog = [("MOV", 5), ("ADD", 10)]
    assert vm.run(prog) == 15
    try:
        vm.run([("JMP", 0)]) # Loop
        assert False
    except ValueError:
        pass
    print("Day 372 eBPF Verifier tests passed!")
