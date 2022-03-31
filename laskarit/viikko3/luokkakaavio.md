```mermaid
classDiagram
	Pelilauta "40" -- "1" Ruutu
	Ruutu --|> SeuraavaRuutu
	Pelinappula "*" -- "1" Ruutu
	Pelaaja "1" -- "1" Pelinappula
	Noppa  "2" <.. "*" Pelinappula
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
