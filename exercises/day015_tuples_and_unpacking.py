# Day 15: Tuples and Unpacking

# Packing and unpacking
point = (10, 20, 30)
x, y, z = point
print(f"Coordinates: x={x}, y={y}, z={z}")

# Starred unpacking
first, *middle, last = [10, 20, 30, 40, 50, 60]
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Returning multiple values from a function
def get_stats(data):
    return min(data), max(data), sum(data) / len(data)

minimum, maximum, average = get_stats([12, 45, 67, 89, 34])
print(f"Min: {minimum}, Max: {maximum}, Avg: {average:.2f}")
