# SLE-2: BFS vs DFS Performance Analysis

## Course
02AML204 – Introduction to Artificial Intelligence

## Experiment
SLE-2 – Profiling Report (Empirical Performance Analysis)

## Student Information

- Name: Vaishnavi Punde
- PRN: 25UAM066
- Division: A

---

## 1. Objective

The objective of this experiment is to perform an empirical performance
analysis of Breadth-First Search (BFS) and Depth-First Search (DFS).

The algorithms are compared using:

- Execution time
- Average execution time
- Best and worst execution time
- Number of nodes expanded
- Path found by each algorithm

---

## 2. Algorithms Used

### Breadth-First Search (BFS)

BFS explores the graph level by level. It uses a queue to store nodes
that need to be explored.

### Depth-First Search (DFS)

DFS explores one branch deeply before backtracking. It uses a stack-based
approach.

---

## 3. Problem Used

A small graph was used for the experiment.

- Start Node: A
- Goal Node: W

Both BFS and DFS were executed on the same graph to maintain a fair
comparison.

---

## 4. Profiling Method

Python's `time.perf_counter()` was used to measure execution time.

Each algorithm was executed three times.

The following measurements were recorded:

- Run 1 execution time
- Run 2 execution time
- Run 3 execution time
- Best execution time
- Average execution time
- Worst execution time
- Nodes expanded

Average execution time was calculated as:

Average Time = (Run 1 + Run 2 + Run 3) / 3

---

## 5. Comparison Table

The actual values collected during execution are recorded below.

| Metric | BFS | DFS |
|---|---:|---:|
| Run 1 Time (ms) | ______ | ______ |
| Run 2 Time (ms) | ______ | ______ |
| Run 3 Time (ms) | ______ | ______ |
| Best Time (ms) | ______ | ______ |
| Average Time (ms) | ______ | ______ |
| Worst Time (ms) | ______ | ______ |
| Nodes Expanded | ______ | ______ |

---

## 6. Observation

BFS and DFS were tested on the same graph and with the same start and
goal nodes.

The execution time was measured three times to obtain more reliable
experimental results. The number of nodes expanded was also recorded.

The actual performance depends on the graph structure, implementation,
and computer used for the experiment.

---

## 7. Justification and Analysis

BFS and DFS were compared using actual execution time and the number of
nodes expanded. Both algorithms were executed three times on the same
graph to maintain a fair comparison.

BFS explores nodes level by level, while DFS explores one branch deeply
before backtracking. The measured execution times provide an empirical
comparison of their implementations.

The number of nodes expanded indicates how much of the search space was
explored before reaching the goal. The experimental results are used
for the final analysis rather than relying only on theoretical
complexity.

For a larger problem, the search space may increase and the practical
difference between the algorithms may become more noticeable.

---

## 8. Tools Used

- Python
- Visual Studio Code
- Python `time` module
- GitHub
- ChatGPT for AI-assisted learning and documentation

---

## 9. Files in This Repository

```text
IAI_SLE-2/
│
├── SLE2_BFS_vs_DFS.py
├── README.md
└── AI_CONTRIBUTION_LOG.md
## Course
02AML204 – Introduction to Artificial Intelligence

## Project Title
Empirical Performance Analysis of BFS and DFS

## Objective
The objective of this project is to compare the performance of two
uninformed search algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)

Both algorithms are applied to the same graph and their performance
is measured using execution time and number of nodes expanded.

## Problem Used
A small graph is used for the search experiment.

Start Node: A  
Goal Node: L

The same graph and start/goal nodes are used for both BFS and DFS
to make the comparison fair.

## Algorithms

### 1. Breadth First Search (BFS)
BFS explores nodes level by level. It uses a queue to store nodes
that are waiting to be explored.

### 2. Depth First Search (DFS)
DFS explores one branch as deeply as possible before backtracking.
It uses a stack to manage the search.

## Profiling Method

The Python `time` module is used to measure execution time.

Each algorithm is executed 3 times.

The following metrics are collected:

- Execution time in milliseconds
- Number of nodes expanded
- Average execution time

## Experimental Results

| Run | BFS Time (ms) | BFS Nodes | DFS Time (ms) | DFS Nodes |
|-----|---------------|-----------|---------------|-----------|
| 1 | 0.038200 | 12 | 0.019500 | 12 |
| 2 | 0.011200 | 12 | 0.010300 | 12 |
| 3 | 0.008600 | 12 | 0.008900 | 12 |
| Average | 0.019333 | 12 | 0.012900 | 12 |

## Observation

In this experiment, DFS has a lower average execution time than BFS.
Both algorithms expanded 12 nodes.

The measured result is based on this particular graph and the
execution environment used during the experiment.

## Conclusion

This experiment helped in understanding the practical performance
of BFS and DFS. Both algorithms were tested on the same graph and
their execution time and nodes expanded were recorded. The experiment
also showed how profiling can be used to compare search algorithms
using actual measurements rather than only theoretical analysis.

## Tools and Technologies

- Python
- Visual Studio Code
- GitHub
- Python time module

## Files

- `SLE2_BFS_vs_DFS.py` – Python implementation of BFS and DFS
- `README.md` – Project documentation
- `AI_CONTRIBUTION_LOG.md` – AI contribution and work record

## Author

Student – B.Tech. CSE (AI & ML)