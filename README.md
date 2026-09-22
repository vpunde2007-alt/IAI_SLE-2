# SLE-2: BFS vs DFS Empirical Performance Analysis

## Introduction

This project implements and experimentally compares two uninformed
search algorithms:

- Breadth First Search (BFS)
- Depth First Search (DFS)

The objective is to measure their execution performance using actual
experiments and profiling.

---

## Problem Statement

The experiment compares BFS and DFS on the same connected graph.

The graph contains:

- Number of nodes: 750
- Start node: 0
- Goal node: 749

Both algorithms search for the same goal node.

---

## Algorithms Used

### 1. Breadth First Search (BFS)

BFS explores nodes level by level using a queue.

In this implementation, Python's `deque` is used to implement the
queue.

### 2. Depth First Search (DFS)

DFS explores one branch deeply before backtracking.

In this implementation, a Python list is used as a stack.

---

## Graph Generation

A connected graph with 750 nodes is generated using Python.

A fixed random seed is used:

```python
random.seed(42)