@startuml

title C3 - Component Diagram

rectangle "Search Engine" {

    rectangle "BFS Algorithm" as BFS

    rectangle "DFS Algorithm" as DFS

    rectangle "Frontier Manager" as Frontier

    rectangle "Goal Test" as Goal

    rectangle "Path Reconstructor" as Path
}

BFS --> Frontier : Explore Nodes
DFS --> Frontier : Explore Nodes

Frontier --> Goal : Current Node

Goal --> Path : Goal Found

@enduml