```mermaid
sequenceDiagram
  participant main
  participant moottori
  participant FuelTank
  participant Engine
  moottori ->> FuelTank: fill(40)
  main ->>+ moottori: drive()
  moottori ->> Engine: start()
  Engine ->> FuelTank: consume(5)
  FuelTank-->>- moottori: 

