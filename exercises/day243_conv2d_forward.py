"""Day 243: 2D Convolution."""

def conv2d(image, kernel, stride=1):
    h, w = len(image), len(image[0])
    kh, kw = len(kernel), len(kernel[0])
    out_h = (h - kh) // stride + 1
    out_w = (w - kw) // stride + 1
    out = [[0.0] * out_w for _ in range(out_h)]

    for i in range(out_h):
        for j in range(out_w):
            s = 0.0
            for ki in range(kh):
                for kj in range(kw):
                    s += image[i * stride + ki][j * stride + kj] * kernel[ki][kj]
            out[i][j] = s
    return out

if __name__ == "__main__":
    img = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    kern = [
        [1, 0],
        [0, 1]
    ]
    res = conv2d(img, kern)
    assert res[0][0] == 6 # 1*1 + 5*1
    assert res[1][1] == 14 # 5*1 + 9*1
    print("Day 243 Conv2D tests passed!")
