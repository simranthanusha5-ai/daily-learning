"""Day 325: Syscall Tracer (Strace)."""

class SyscallTracer:
    def __init__(self):
        self.trace_log = []

    def trace_syscall(self, pid, syscall_name, args, ret_val):
        entry = {
            "pid": pid,
            "call": f"{syscall_name}({', '.join(map(str, args))})",
            "ret": ret_val
        }
        self.trace_log.append(entry)

    def report(self):
        return [f"[{e['pid']}] {e['call']} = {e['ret']}" for e in self.trace_log]

if __name__ == "__main__":
    tracer = SyscallTracer()
    tracer.trace_syscall(101, "openat", ["AT_FDCWD", "/etc/hosts", "O_RDONLY"], 3)
    tracer.trace_syscall(101, "read", [3, "0x7ffd", 1024], 64)
    rep = tracer.report()
    assert "openat(AT_FDCWD, /etc/hosts, O_RDONLY) = 3" in rep[0]
    print("Day 325 Syscall Tracer tests passed!")
