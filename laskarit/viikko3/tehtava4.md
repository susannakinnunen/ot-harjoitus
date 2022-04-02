```mermaid
sequenceDiagram
  participant main
  participant laitehallinto
  participant ratikka6
  participant bussi 244
  participant lippu_luukku
  participant kallen_kortti
  main ->> laitehallinto: lisaa_lataaja(rautatietori)
  main ->> laitehallinto: lisaa_lataaja(ratikka6)
  main ->> laitehallinto: lisaa_lataaja(bussi244)
  main ->> +lippu_luukku: osta_matkakortti("Kalle")
  lippu_luukku -->> -main: uusi_kortti
  
  
  
