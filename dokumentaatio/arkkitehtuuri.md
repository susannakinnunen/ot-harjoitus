```mermaid
classDiagram
  UI -- StretchingService
  StretchingService -- Repositories



```mermaid
sequenceDiagram
actor User
User ->> UI: "A"
UI ->> BodypartView: show_bodyparts()
BodypartView ->> StretchingSerive: get_all_bodyparts()
StretchingServivce ->> BodypartRepositories: find_all()
    
    
