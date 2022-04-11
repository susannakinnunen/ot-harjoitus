```mermaid
classDiagram
  ui --> UserService
  ui --> StretchService
  UserService --> User
  StretchService --> Bodypart
  StretchService --> Stretch
  StretchService --> BodypartStretch
  User --> Bodypart
  User --> BodypartStretch
  User --> Stretch
  BodypartStretch --> Bodypart
  BodypartStretch --> Stretch
  Bodypart <-- Stretch
  class User{
    username
    password
  }
  class Bodypart{
    add_bodypart
    find_all
   }
   class Stretch{
    add_stretch
    find_stretch
   }
   class BodypartStretch{
   add_combination(bodypart, stretch)
   }
    
    
