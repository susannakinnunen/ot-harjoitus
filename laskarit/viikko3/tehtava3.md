```mermaid
sequenceDiagram
  participant main
  participant moottori
  participant FuelTank
  participant Engine
  moottori ->> FuelTank: fill(40)
  
