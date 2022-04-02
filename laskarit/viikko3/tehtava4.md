```mermaid
sequenceDiagram
  participant main
  participant laitehallinto
  participant rautatientori
  participant ratikka6
  participant bussi244
  participant lippu_luukku
  participant kallen_kortti
  main ->> laitehallinto: lisaa_lataaja(rautatietori)
  main ->> laitehallinto: lisaa_lataaja(ratikka6)
  main ->> laitehallinto: lisaa_lataaja(bussi244)
  main ->> +lippu_luukku: osta_matkakortti("Kalle")
  lippu_luukku -->> -main: uusi_kortti
  main ->> rautatientori: (kallen_kortti, 3)
  rautatientori ->> kallen_kortti: kasvata_arvoa(3)
  main ->> +ratikka6:osta_lippu(kallen_kortti, 0)
  ratikka6 ->> kallen_kortti: vahenna_arvoa(1,5)
  ratikka6 ->> -main: True
  main ->> +bussi244: osta_lippu(kallen_kortti, 2)
  bussi244 ->> -main: False
  
  
