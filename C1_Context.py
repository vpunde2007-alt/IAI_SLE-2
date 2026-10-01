<<<<<<< HEAD
@startuml

title C1 - Context Diagram

actor User

rectangle "BFS & DFS\nGraph Search System" as System

rectangle "Search Result\n(Path / Goal Status /\nNodes Expanded)" as Result

User --> System : Graph\nStart Node\nGoal Node\nAlgorithm
System --> Result : Search Result

=======
@startuml

title C1 - Context Diagram

actor User

rectangle "BFS & DFS\nGraph Search System" as System

rectangle "Search Result\n(Path / Goal Status /\nNodes Expanded)" as Result

User --> System : Graph\nStart Node\nGoal Node\nAlgorithm
System --> Result : Search Result

>>>>>>> 5be3a4c (Add SLE-3 C4 architecture diagrams and code)
@enduml