"""Day 361: LoRA Forward Pass."""

class LoRALayer:
    def __init__(self, in_dim, out_dim, rank=2, alpha=1.0):
        self.w0 = [[0.1] * in_dim for _ in range(out_dim)]
        self.A = [[0.05] * in_dim for _ in range(rank)]
        self.B = [[0.0] * rank for _ in range(out_dim)] # Init B to 0
        self.scale = alpha / rank

    def forward(self, x):
        # Base output: W0 @ x
        out = [sum(w_row[i] * x[i] for i in range(len(x))) for w_row in self.w0]
        # LoRA delta: (alpha / r) * (B @ A @ x)
        Ax = [sum(a_row[i] * x[i] for i in range(len(x))) for a_row in self.A]
        BAx = [sum(b_row[i] * Ax[i] for i in range(len(Ax))) for b_row in self.B]
        return [o + self.scale * delta for o, delta in zip(out, BAx)]

if __name__ == "__main__":
    lora = LoRALayer(in_dim=3, out_dim=2, rank=1)
    res = lora.forward([1.0, 1.0, 1.0])
    assert abs(res[0] - 0.3) < 1e-6
    print("Day 361 LoRA tests passed!")
