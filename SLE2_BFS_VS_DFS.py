from collections import deque
import time

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['I', 'J'],
    'F': ['K'],
    'G': ['L'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': []
}

start = 'A'
goal = 'L'


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    nodes_expanded = 0

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(path + [neighbour])

    return None, nodes_expanded


# ---------------- DFS ----------------
def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    nodes_expanded = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(path + [neighbour])

    return None, nodes_expanded


# ---------------- Run 3 Times ----------------

bfs_times = []
dfs_times = []

bfs_nodes = []
dfs_nodes = []

for i in range(3):

    # BFS
    start_time = time.perf_counter()
    bfs_path, nodes = bfs(graph, start, goal)
    end_time = time.perf_counter()

    bfs_time = (end_time - start_time) * 1000

    bfs_times.append(bfs_time)
    bfs_nodes.append(nodes)

    # DFS
    start_time = time.perf_counter()
    dfs_path, nodes = dfs(graph, start, goal)
    end_time = time.perf_counter()

    dfs_time = (end_time - start_time) * 1000

    dfs_times.append(dfs_time)
    dfs_nodes.append(nodes)


# ---------------- Average ----------------

avg_bfs_time = sum(bfs_times) / 3
avg_dfs_time = sum(dfs_times) / 3

avg_bfs_nodes = sum(bfs_nodes) / 3
avg_dfs_nodes = sum(dfs_nodes) / 3


# ---------------- Output ----------------

print("========== BFS vs DFS ==========")

print("\nBFS Path:")
print(" -> ".join(bfs_path))

print("\nDFS Path:")
print(" -> ".join(dfs_path))


print("\n========== RUN RESULTS ==========")

for i in range(3):
    print("\nRun", i + 1)

    print("BFS Time: {:.6f} ms".format(bfs_times[i]))
    print("BFS Nodes Expanded:", bfs_nodes[i])

    print("DFS Time: {:.6f} ms".format(dfs_times[i]))
    print("DFS Nodes Expanded:", dfs_nodes[i])


print("\n========== AVERAGE RESULTS ==========")

print("BFS Average Time: {:.6f} ms".format(avg_bfs_time))
print("DFS Average Time: {:.6f} ms".format(avg_dfs_time))

print("BFS Average Nodes:", avg_bfs_nodes)
print("DFS Average Nodes:", avg_dfs_nodes)


print("\n========== COMPARISON ==========")

if avg_bfs_time < avg_dfs_time:
    print("BFS has lower average execution time.")
else:
    print("DFS has lower average execution time.")

if avg_bfs_nodes < avg_dfs_nodes:
    print("BFS expanded fewer nodes.")
elif avg_dfs_nodes < avg_bfs_nodes:
    print("DFS expanded fewer nodes.")
else:
    print("Both expanded the same number of nodes.")