"""Day 272: Stack-based Bytecode VM."""

class VirtualMachine:
    PUSH = 1
    ADD = 2
    SUB = 3
    HALT = 4

    def __init__(self):
        self.stack = []

    def run(self, bytecode):
        ip = 0
        while ip < len(bytecode):
            op = bytecode[ip]
            if op == self.PUSH:
                ip += 1
                self.stack.append(bytecode[ip])
            elif op == self.ADD:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif op == self.SUB:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
            elif op == self.HALT:
                break
            ip += 1
        return self.stack[-1] if self.stack else None

if __name__ == "__main__":
    vm = VirtualMachine()
    # (10 + 20) - 5
    program = [vm.PUSH, 10, vm.PUSH, 20, vm.ADD, vm.PUSH, 5, vm.SUB, vm.HALT]
    assert vm.run(program) == 25
    print("Day 272 Bytecode VM tests passed!")
