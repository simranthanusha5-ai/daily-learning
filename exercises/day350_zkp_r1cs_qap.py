"""Day 350: R1CS Constraint Verification."""

def dot(vec1, vec2):
    return sum(a * b for a, b in zip(vec1, vec2))

def verify_r1cs(A, B, C, witness):
    # For every constraint row i: (A_i . w) * (B_i . w) == C_i . w
    for a_row, b_row, c_row in zip(A, B, C):
        if dot(a_row, witness) * dot(b_row, witness) != dot(c_row, witness):
            return False
    return True

if __name__ == "__main__":
    # x * x = out where w = [1, x, out]
    # (0*1 + 1*x + 0*out) * (0*1 + 1*x + 0*out) = (0*1 + 0*x + 1*out)
    A = [[0, 1, 0]]
    B = [[0, 1, 0]]
    C = [[0, 0, 1]]
    valid_w = [1, 3, 9]
    invalid_w = [1, 3, 10]
    assert verify_r1cs(A, B, C, valid_w) is True
    assert verify_r1cs(A, B, C, invalid_w) is False
    print("Day 350 R1CS ZKP tests passed!")
