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
# SLE-3: Full C4 Model – BFS vs DFS Graph Search

## 1. Introduction

This SLE-3 project presents the **Full C4 Model** for a **BFS and DFS Graph Search System**.

The C4 model is used to represent the software system at four different levels of detail:

* **C1 – Context**
* **C2 – Container**
* **C3 – Component**
* **C4 – Code**

The purpose of this project is to understand the structure of the BFS and DFS graph search system and represent its architecture from a high-level system view to the code level.

---

## 2. Problem Statement

Design and represent a graph search system that uses **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** and document its software architecture using the complete C4 model.

---

## 3. Objectives

* To understand the C4 software architecture model.
* To create the C1 Context diagram.
* To create the C2 Container diagram.
* To create the C3 Component diagram.
* To create the C4 Code-level representation.
* To understand the relationship between system architecture and source code.
* To implement and demonstrate BFS and DFS graph search.

---

# 4. C4 Model

## C1 – Context Level

The **C1 Context diagram** provides a high-level view of the complete system.

### Main Elements

* **User / Operator**
* **BFS & DFS Graph Search System**
* **Search Result / Output**

### System Interaction

The user provides the required graph information, start node, goal node and search algorithm.

The BFS and DFS Graph Search System processes the input and provides the search result.

### C1 Diagram

The C1 diagram is stored in:

```text
c1.png
```

---

## C2 – Container Level

The **C2 Container diagram** divides the system into major functional containers.

### Containers

### 1. Input Module

Accepts:

* Graph
* Start node
* Goal node
* Search algorithm

### 2. Graph Manager

Manages:

* Graph nodes
* Graph edges

### 3. Search Engine

Executes:

* BFS
* DFS

### 4. Visited / Memory Manager

Keeps track of visited nodes during graph traversal.

### 5. Output Module

Provides:

* Search path
* Goal status
* Nodes expanded

### Container Flow

```text
Input Module
      ↓
Graph Manager
      ↓
Search Engine
      ↓
Visited / Memory Manager
      ↓
Output Module
```

### C2 Diagram

The C2 diagram is stored in:

```text
c2.png
```

---

# 5. C3 – Component Level

The **C3 Component diagram** focuses on the **Search Engine** container.

The Search Engine contains the main components required for BFS and DFS.

### Components

### BFS Algorithm

Performs Breadth-First Search by exploring nodes level by level.

### DFS Algorithm

Performs Depth-First Search by exploring a branch deeply before backtracking.

### Frontier Manager

Manages the nodes that are waiting to be explored.

### Goal Test

Checks whether the current node is the required goal node.

### Path Reconstructor

Reconstructs the path from the start node to the goal node.

### Component Flow

```text
BFS / DFS Algorithm
        ↓
Frontier Manager
        ↓
Goal Test
        ↓
Path Reconstructor
```

### C3 Diagram

The C3 diagram is stored in:

```text
c3.png
```

---

# 6. C4 – Code Level

The **C4 Code level** represents the main implementation structure of the BFS and DFS system.

### Main Classes and Functions

```text
Graph
 ├── add_node()
 └── add_edge()

Search Engine
 ├── bfs()
 └── dfs()

Goal Test
 └── goal_test()

Path Reconstructor
 └── reconstruct_path()

Main
 └── main()
```

### Code Responsibilities

| Class / Function     | Responsibility                     |
| -------------------- | ---------------------------------- |
| `Graph`              | Stores graph nodes and edges       |
| `add_node()`         | Adds a node to the graph           |
| `add_edge()`         | Adds an edge between nodes         |
| `bfs()`              | Performs Breadth-First Search      |
| `dfs()`              | Performs Depth-First Search        |
| `goal_test()`        | Checks whether the goal is reached |
| `reconstruct_path()` | Reconstructs the path              |
| `main()`             | Controls program execution         |

### C4 Diagram

The C4 diagram is stored in:

```text
c4.png
```

---

# 7. BFS – Breadth-First Search

BFS is a graph traversal algorithm that explores nodes level by level.

It uses a **queue** to manage the nodes that need to be explored.

### Basic Flow

```text
Start Node
    ↓
Explore Neighbours
    ↓
Explore Next Level
    ↓
Continue Until Goal
```

---

# 8. DFS – Depth-First Search

DFS is a graph traversal algorithm that explores one branch deeply before backtracking.

It uses a **stack** to manage the nodes that need to be explored.

### Basic Flow

```text
Start Node
    ↓
Explore One Branch
    ↓
Go Deeper
    ↓
Backtrack
    ↓
Explore Next Branch
```

---

# 9. Project Files

```text
SLE3
│
├── C1_Context.py
├── C2_Container.py
├── C3_Component.py
├── C4_Code.py
│
├── c1.png
├── c2.png
├── c3.png
├── c4.png
│
├── README.md
└── AI_CONTRIBUTION_LOG.md
```

---

# 10. Technologies Used

* Python
* PlantUML
* Visual Studio Code
* Git
* GitHub
* Markdown

---

# 11. How to Run

Open the project folder in **Visual Studio Code**.

Open the VS Code terminal:

```text
Terminal → New Terminal
```

Run the Python files using:

```bash
python C1_Context.py
```

```bash
python C2_Container.py
```

```bash
python C3_Component.py
```

```bash
python C4_Code.py
```

---

# 12. Architecture Flow

The complete C4 model can be understood as:

```text
C1 – Context
      ↓
C2 – Containers
      ↓
C3 – Components
      ↓
C4 – Code
```

Each level provides more detailed information about the BFS and DFS Graph Search System.

---

# 13. GitHub

The project is maintained using **Git and GitHub**.

Git is used for version control, while GitHub is used to store and manage the project files.

---

# 14. AI Contribution

AI tools were used as a supporting resource during the development of this SLE.

AI assistance was used for:

* Understanding the C4 model.
* Structuring C1, C2, C3 and C4 diagrams.
* Understanding BFS and DFS implementation.
* Debugging programming errors.
* Preparing project documentation.
* Understanding Git and GitHub commands.

The AI-assisted content was reviewed and adapted by the student for the final SLE submission.

Detailed AI usage is documented in:

```text
AI_CONTRIBUTION_LOG.md
```

---

# 15. Conclusion

This SLE demonstrates the **Full C4 Model** for a BFS and DFS Graph Search System.

The project represents the system at four levels: **Context, Container, Component and Code**. This provides a clear understanding of the system architecture and its relationship with the implementation.

The project also demonstrates the use of **Python, PlantUML, Visual Studio Code, Git and GitHub** for software development and documentation.
