@startuml

title C4 - Code Level

class Graph {
    +add_node(node)
    +add_edge(u, v)
}

class SearchEngine {
    +bfs(graph, start, goal)
    +dfs(graph, start, goal)
}

class GoalTest {
    +goal_test(current, goal)
}

class PathReconstructor {
    +reconstruct_path(parent, start, goal)
}

class Main {
    +main()
}

Main --> Graph : creates
Main --> SearchEngine : calls
SearchEngine --> GoalTest : checks goal
SearchEngine --> PathReconstructor : creates path

@enduml