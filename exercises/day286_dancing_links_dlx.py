"""Day 286: Dancing Links DLX."""

class DLXNode:
    def __init__(self, col=None):
        self.left = self
        self.right = self
        self.up = self
        self.down = self
        self.col = col

class DLXMatrix:
    def __init__(self, num_cols):
        self.head = DLXNode()
        self.cols = []
        curr = self.head
        for c in range(num_cols):
            col_node = DLXNode()
            col_node.left = curr
            curr.right = col_node
            self.cols.append(col_node)
            curr = col_node
        self.head.left = curr
        curr.right = self.head

    def cover(self, c):
        c.right.left = c.left
        c.left.right = c.right

    def uncover(self, c):
        c.right.left = c
        c.left.right = c

if __name__ == "__main__":
    dlx = DLXMatrix(3)
    c0 = dlx.cols[0]
    dlx.cover(c0)
    assert dlx.head.right == dlx.cols[1]
    dlx.uncover(c0)
    assert dlx.head.right == c0
    print("Day 286 Dancing Links tests passed!")
