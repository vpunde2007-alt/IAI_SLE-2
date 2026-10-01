@startuml

title C2 - Container Diagram

rectangle "Input Module\n\nGraph\nStart Node\nGoal Node\nAlgorithm" as Input

rectangle "Graph Manager\n\nStores Nodes\nand Edges" as Graph

rectangle "Search Engine\n\nBFS / DFS" as Search

rectangle "Visited / Memory Manager\n\nTracks Visited Nodes" as Memory

rectangle "Output Module\n\nPath\nGoal Status\nNodes Expanded" as Output

Input --> Graph : Graph Data
Graph --> Search : Graph
Search --> Memory : Visited Nodes
Memory --> Search : Memory Information
Search --> Output : Search Result
@enduml