from collections import deque
import random
import timeit


# ============================================================
# SETTINGS
# ============================================================

NUM_NODES = 750
START_NODE = 0
GOAL_NODE = 749

# Number of timing runs
NUM_RUNS = 3

# Number of times execute_profiling() is repeated
# This gives py-spy more work to sample.
PROFILE_RUNS = 15


# ============================================================
# CREATE GRAPH
# ============================================================

random.seed(42)

# Building a connected graph
graph = {i: [] for i in range(NUM_NODES)}

for i in range(NUM_NODES - 1):
    graph[i].append(i + 1)

for i in range(NUM_NODES):

    extra_edges = random.sample(
        range(NUM_NODES),
        min(15, NUM_NODES - 1)
    )

    for target in extra_edges:

        if target != i and target not in graph[i]:
            graph[i].append(target)


# ============================================================
# BFS
# ============================================================

def run_bfs(graph, start, goal):

    nodes_expanded = 0
    visited = set()
    queue = deque([start])

    start_time = timeit.default_timer()

    found = False

    while queue:

        # Small workload so py-spy has time to sample
        for _ in range(15000):
            pass

        current = queue.popleft()

        if current not in visited:

            visited.add(current)
            nodes_expanded += 1

            if current == goal:

                found = True
                break

            for neighbor in graph[current]:

                if neighbor not in visited:
                    queue.append(neighbor)

    end_time = timeit.default_timer()

    execution_time_ms = (
        end_time - start_time
    ) * 1000

    return execution_time_ms, nodes_expanded, found


# ============================================================
# DFS
# ============================================================

def run_dfs(graph, start, goal):

    nodes_expanded = 0
    visited = set()
    stack = [start]

    start_time = timeit.default_timer()

    found = False

    while stack:

        # Small workload so py-spy has time to sample
        for _ in range(3500):
            pass

        current = stack.pop()

        if current not in visited:

            visited.add(current)
            nodes_expanded += 1

            if current == goal:

                found = True
                break

            for neighbor in reversed(graph[current]):

                if neighbor not in visited:
                    stack.append(neighbor)

    end_time = timeit.default_timer()

    execution_time_ms = (
        end_time - start_time
    ) * 1000

    return execution_time_ms, nodes_expanded, found


# ============================================================
# EXECUTION PROFILING
# ============================================================

def execute_profiling():

    print("=" * 70)
    print("       SLE-2: EMPIRICAL PERFORMANCE ANALYSIS")
    print("              Comparison: BFS vs DFS")
    print("=" * 70)

    print("\nProblem:")
    print("Number of Nodes =", NUM_NODES)
    print("Start Node      =", START_NODE)
    print("Goal Node       =", GOAL_NODE)
    print("Number of Runs  =", NUM_RUNS)

    # ========================================================
    # BFS RUNS
    # ========================================================

    print("\n" + "-" * 70)
    print("BFS - Breadth First Search")
    print("-" * 70)

    bfs_times = []
    bfs_nodes_list = []

    bfs_found = False

    for i in range(NUM_RUNS):

        t, n, found = run_bfs(
            graph,
            START_NODE,
            GOAL_NODE
        )

        bfs_times.append(t)
        bfs_nodes_list.append(n)
        bfs_found = found

        print(
            "Run {}: Time = {:.5f} ms, Nodes Expanded = {}".format(
                i + 1,
                t,
                n
            )
        )

    # ========================================================
    # DFS RUNS
    # ========================================================

    print("\n" + "-" * 70)
    print("DFS - Depth First Search")
    print("-" * 70)

    dfs_times = []
    dfs_nodes_list = []

    dfs_found = False

    for i in range(NUM_RUNS):

        t, n, found = run_dfs(
            graph,
            START_NODE,
            GOAL_NODE
        )

        dfs_times.append(t)
        dfs_nodes_list.append(n)
        dfs_found = found

        print(
            "Run {}: Time = {:.5f} ms, Nodes Expanded = {}".format(
                i + 1,
                t,
                n
            )
        )

    # ========================================================
    # BFS CALCULATIONS
    # ========================================================

    bfs_best = min(bfs_times)
    bfs_worst = max(bfs_times)
    bfs_avg = sum(bfs_times) / NUM_RUNS

    avg_bfs_nodes = (
        sum(bfs_nodes_list) / NUM_RUNS
    )

    # ========================================================
    # DFS CALCULATIONS
    # ========================================================

    dfs_best = min(dfs_times)
    dfs_worst = max(dfs_times)
    dfs_avg = sum(dfs_times) / NUM_RUNS

    avg_dfs_nodes = (
        sum(dfs_nodes_list) / NUM_RUNS
    )

    # ========================================================
    # FINAL COMPARISON
    # ========================================================

    print("\n" + "=" * 70)
    print("                         FINAL COMPARISON")
    print("=" * 70)

    print(
        "{:<35} {:<15} {:<15}".format(
            "Metric",
            "BFS",
            "DFS"
        )
    )

    print("-" * 70)

    print(
        "{:<35} {:<15.5f} {:<15.5f}".format(
            "Best Case Time (ms)",
            bfs_best,
            dfs_best
        )
    )

    print(
        "{:<35} {:<15.5f} {:<15.5f}".format(
            "Worst Case Time (ms)",
            bfs_worst,
            dfs_worst
        )
    )

    print(
        "{:<35} {:<15.5f} {:<15.5f}".format(
            "Average Case Time (ms)",
            bfs_avg,
            dfs_avg
        )
    )

    print("-" * 70)

    print(
        "{:<35} {:<15.5f} {:<15.5f}".format(
            "Run 1 Time (ms)",
            bfs_times[0],
            dfs_times[0]
        )
    )

    print(
        "{:<35} {:<15.5f} {:<15.5f}".format(
            "Run 2 Time (ms)",
            bfs_times[1],
            dfs_times[1]
        )
    )

    print(
        "{:<35} {:<15.5f} {:<15.5f}".format(
            "Run 3 Time (ms)",
            bfs_times[2],
            dfs_times[2]
        )
    )

    print("-" * 70)

    print(
        "{:<35} {:<15.2f} {:<15.2f}".format(
            "Average Nodes Expanded",
            avg_bfs_nodes,
            avg_dfs_nodes
        )
    )

    print(
        "{:<35} {:<15} {:<15}".format(
            "Goal Found",
            str(bfs_found),
            str(dfs_found)
        )
    )

    print("=" * 70)

    print("\nProfiling completed successfully.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    # Run the complete experiment 15 times
    # so py-spy gets enough execution time to sample.
    for _ in range(PROFILE_RUNS):

        execute_profiling()