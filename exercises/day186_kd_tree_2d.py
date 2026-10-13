"""Day 186: 2D KD-Tree."""

class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

class KDTree2D:
    def __init__(self, points):
        self.root = self._build(points, depth=0)

    def _build(self, points, depth):
        if not points:
            return None
        axis = depth % 2
        points.sort(key=lambda p: p[axis])
        mid = len(points) // 2
        return KDNode(
            point=points[mid],
            axis=axis,
            left=self._build(points[:mid], depth + 1),
            right=self._build(points[mid + 1:], depth + 1)
        )

    def nearest(self, target):
        best = [float('inf'), None]

        def _dist_sq(p1, p2):
            return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

        def _search(node):
            if not node: return
            d = _dist_sq(node.point, target)
            if d < best[0]:
                best[0] = d
                best[1] = node.point
            axis = node.axis
            diff = target[axis] - node.point[axis]
            first = node.left if diff < 0 else node.right
            second = node.right if diff < 0 else node.left
            _search(first)
            if diff**2 < best[0]:
                _search(second)

        _search(self.root)
        return best[1]

if __name__ == "__main__":
    pts = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
    kd = KDTree2D(pts)
    nn = kd.nearest((9, 2))
    assert nn in [(8, 1), (7, 2)]
    print("Day 186 KD-Tree tests passed!")
