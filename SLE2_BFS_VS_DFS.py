import time
from collections import deque


# -----------------------------
# BFS Algorithm
# -----------------------------
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_expanded = 0

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# -----------------------------
# DFS Algorithm
# -----------------------------
def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# -----------------------------
# Performance Measurement
# -----------------------------
def measure_algorithm(algorithm, graph, start, goal, runs=3):

    times = []
    nodes = []

    for i in range(runs):

        start_time = time.perf_counter()

        path, expanded = algorithm(graph, start, goal)

        end_time = time.perf_counter()

        elapsed = (end_time - start_time) * 1000

        times.append(elapsed)
        nodes.append(expanded)

    best_time = min(times)
    average_time = sum(times) / len(times)
    worst_time = max(times)

    average_nodes = sum(nodes) / len(nodes)

    return (
        path,
        times,
        best_time,
        average_time,
        worst_time,
        average_nodes
    )


# -----------------------------
# Graph
# -----------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': ['P'],
    'I': ['Q'],
    'J': ['R'],
    'K': ['S'],
    'L': ['T'],
    'M': ['U'],
    'N': ['V'],
    'O': ['W'],
    'P': [],
    'Q': [],
    'R': [],
    'S': [],
    'T': [],
    'U': [],
    'V': [],
    'W': []
}


# -----------------------------
# Main Program
# -----------------------------
def main():

    start = 'A'
    goal = 'W'
    runs = 3

    print("=" * 65)
    print("        SLE-2: BFS vs DFS PERFORMANCE ANALYSIS")
    print("=" * 65)

    print("\nStart Node      :", start)
    print("Goal Node       :", goal)
    print("Number of Runs  :", runs)

    # -------------------------
    # BFS Measurement
    # -------------------------
    (
        bfs_path,
        bfs_times,
        bfs_best,
        bfs_average,
        bfs_worst,
        bfs_nodes
    ) = measure_algorithm(
        bfs, graph, start, goal, runs
    )

    # -------------------------
    # DFS Measurement
    # -------------------------
    (
        dfs_path,
        dfs_times,
        dfs_best,
        dfs_average,
        dfs_worst,
        dfs_nodes
    ) = measure_algorithm(
        dfs, graph, start, goal, runs
    )

    # -------------------------
    # BFS Results
    # -------------------------
    print("\n" + "-" * 65)
    print("                         BFS RESULTS")
    print("-" * 65)

    print("Path:", " -> ".join(bfs_path))

    print("\nExecution Times:")
    print("Run 1 Time       : {:.6f} ms".format(bfs_times[0]))
    print("Run 2 Time       : {:.6f} ms".format(bfs_times[1]))
    print("Run 3 Time       : {:.6f} ms".format(bfs_times[2]))

    print("\nBest Time        : {:.6f} ms".format(bfs_best))
    print("Average Time     : {:.6f} ms".format(bfs_average))
    print("Worst Time       : {:.6f} ms".format(bfs_worst))
    print("Nodes Expanded   : {:.2f}".format(bfs_nodes))

    # -------------------------
    # DFS Results
    # -------------------------
    print("\n" + "-" * 65)
    print("                         DFS RESULTS")
    print("-" * 65)

    print("Path:", " -> ".join(dfs_path))

    print("\nExecution Times:")
    print("Run 1 Time       : {:.6f} ms".format(dfs_times[0]))
    print("Run 2 Time       : {:.6f} ms".format(dfs_times[1]))
    print("Run 3 Time       : {:.6f} ms".format(dfs_times[2]))

    print("\nBest Time        : {:.6f} ms".format(dfs_best))
    print("Average Time     : {:.6f} ms".format(dfs_average))
    print("Worst Time       : {:.6f} ms".format(dfs_worst))
    print("Nodes Expanded   : {:.2f}".format(dfs_nodes))

    # -----------------------------
    # Comparison Table
    # -----------------------------
    print("\n" + "=" * 65)
    print("                    COMPARISON TABLE")
    print("=" * 65)

    print("{:<25} {:<18} {:<18}".format(
        "Metric", "BFS", "DFS"
    ))

    print("-" * 65)

    print("{:<25} {:<18.6f} {:<18.6f}".format(
        "Best Time (ms)",
        bfs_best,
        dfs_best
    ))

    print("{:<25} {:<18.6f} {:<18.6f}".format(
        "Average Time (ms)",
        bfs_average,
        dfs_average
    ))

    print("{:<25} {:<18.6f} {:<18.6f}".format(
        "Worst Time (ms)",
        bfs_worst,
        dfs_worst
    ))

    print("{:<25} {:<18.2f} {:<18.2f}".format(
        "Nodes Expanded",
        bfs_nodes,
        dfs_nodes
    ))

    print("=" * 65)


# -----------------------------
# Program Start
# -----------------------------
if __name__ == "__main__":
    main()
    