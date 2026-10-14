"""Day 192: Graham Scan Convex Hull."""
import math

def orientation(p, q, r):
    return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

def graham_scan(points):
    p0 = min(points, key=lambda p: (p[1], p[0]))
    def polar_angle(p):
        return math.atan2(p[1] - p0[1], p[0] - p0[0])

    sorted_pts = sorted([p for p in points if p != p0], key=lambda p: (polar_angle(p), (p[0]-p0[0])**2 + (p[1]-p0[1])**2))
    hull = [p0]
    for p in sorted_pts:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], p) >= 0:
            hull.pop()
        hull.append(p)
    return hull

if __name__ == "__main__":
    pts = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
    hull = graham_scan(pts)
    assert (0, 0) in hull
    assert (4, 4) in hull
    print("Day 192 Graham Scan tests passed!")
