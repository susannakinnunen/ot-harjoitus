```mermaid
classDiagram
	Pelilauta "40" -- "1" Ruutu
	Ruutu --|> SeuraavaRuutu
	Pelinappula "*" -- "1" Ruutu
	Pelaaja "1" -- "1" Pelinappula
	Noppa  "2" <.. "*" Pelinappula
  	Ruutu "1" -- "1" Aloitusruutu
  	Ruutu "1" -- "1" Vankila
  	Ruutu "1" -- "1" AsematJaLaitokset
  	Ruutu "1" -- "1" NormaalitKadut
  	Ruutu "1" -- "1" SattumatJaYhteismaa
  	Ruutu -- Toiminto
  	Pelaaja "*" -- "1" NormaalitKadut
  	NormaalitKadut "4" -- "1" Talo
  	NormaalitKadut "1" -- "1" Hotelli
  	SattumaJaYhteismaa "*" -- "*" Kortti
  	Kortti -- Toiminto
  	Pelilauta -- Sijainti
	Aloitusruutu -- Sijainti
	Vankila -- Sijainti
  	class Pelilauta{
	}
	class Ruutu{
	}
	class SeuraavaRuutu{
	}
	class Pelinappula{
	}
	class Pelaaja{
	}
	class Noppa{
	}
	class Aloitusruutu{
 		toiminto
		sijainti
	}
	class Vankila{
  		toiminto
		sijainti
  	}
  	class AsematJaLaitokset{
  		toiminto
  	}
  	class NormaalitKadut{
  		nimi
	  	toiminto
  	}
  	class SattumatJaYhteismaa{
  		toiminto
  	}
  	class NormaalitKadut{
  		toiminto
  }
  	class Kortti{
		toiminto
	}
	class Toiminto{
	}
