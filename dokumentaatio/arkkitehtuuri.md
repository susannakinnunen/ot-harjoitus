```mermaid
classDiagram
  ui --> User
  User --> Bodypart
  BodypartStretch --> Bodypart
  BodypartStretch --> Stretch
  Bodypart --> Stretch
