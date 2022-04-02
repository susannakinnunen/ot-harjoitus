```mermaid
sequenceDiagram
  participant main
  participant laitehallinto
  participant rautatientori
  participant ratikka6
  participant bussi 244
  main ->> laitehallinto: lisaa_lataaja(rautatietori)
  main ->> laitehallinto: lisaa_lataaja(ratikka6)
  main ->> laitehallinto: lisaa_lataaja(bussi244)
  main ->> lippu_luukku: Kioski()
  
