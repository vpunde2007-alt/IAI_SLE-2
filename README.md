# SLE-2: BFS vs DFS Performance Analysis

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