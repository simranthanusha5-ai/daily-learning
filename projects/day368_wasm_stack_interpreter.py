"""Day 368: Mini WebAssembly VM."""

WASM_MAGIC = b"\x00asm"

class WasmVM:
    def __init__(self):
        self.stack = []

    def execute_i32_bytecode(self, opcodes):
        ip = 0
        while ip < len(opcodes):
            op = opcodes[ip]
            if op == 0x41: # i32.const
                val = opcodes[ip + 1]
                self.stack.append(val)
                ip += 2
            elif op == 0x6A: # i32.add
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
                ip += 1
            elif op == 0x0F: # return
                break
            else:
                ip += 1
        return self.stack[-1]

if __name__ == "__main__":
    vm = WasmVM()
    # i32.const 10, i32.const 20, i32.add, return
    code = [0x41, 10, 0x41, 20, 0x6A, 0x0F]
    assert vm.execute_i32_bytecode(code) == 30
    print("Day 368 Wasm Interpreter tests passed!")
