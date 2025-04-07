

````mermaid
graph TD

subgraph Physical_Layer
end

subgraph Structural_Layer
end

subgraph Semantic_Layer
end

subgraph Application_Layer
end

note left of Physical_Layer
    File Format
end note

note right of Physical_Layer
    Storage Model
end note

note right of Structural_Layer
    Data Model
end note

note right of Application_Layer
    Software
end note

Physical_Layer --> Structural_Layer --> Semantic_Layer --> Application_Layer

style Physical_Layer fill:none,stroke-d

````