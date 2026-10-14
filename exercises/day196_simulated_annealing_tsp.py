"""Day 196: Simulated Annealing for TSP."""
import math
import random

def tour_cost(tour, dist_matrix):
    return sum(dist_matrix[tour[i]][tour[(i + 1) % len(tour)]] for i in range(len(tour)))

def simulated_annealing(dist_matrix, temp=100.0, cooling=0.95, iters=500):
    n = len(dist_matrix)
    curr_tour = list(range(n))
    curr_cost = tour_cost(curr_tour, dist_matrix)
    best_tour, best_cost = list(curr_tour), curr_cost

    t = temp
    for _ in range(iters):
        i, j = sorted(random.sample(range(n), 2))
        new_tour = curr_tour[:i] + curr_tour[i:j+1][::-1] + curr_tour[j+1:]
        new_cost = tour_cost(new_tour, dist_matrix)
        delta = new_cost - curr_cost
        if delta < 0 or random.random() < math.exp(-delta / max(t, 1e-9)):
            curr_tour = new_tour
            curr_cost = new_cost
            if curr_cost < best_cost:
                best_cost = curr_cost
                best_tour = list(curr_tour)
        t *= cooling
    return best_tour, best_cost

if __name__ == "__main__":
    matrix = [
        [0, 2, 9, 10],
        [1, 0, 6, 4],
        [15, 7, 0, 8],
        [6, 3, 12, 0]
    ]
    tour, cost = simulated_annealing(matrix, iters=100)
    assert len(tour) == 4
    print("Day 196 Simulated Annealing tests passed!")
