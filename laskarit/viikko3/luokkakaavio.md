```mermaid
classDiagram
	Pelilauta "40" -- "1" Ruutu
	Ruutu --|> SeuraavaRuutu
	Pelinappula "*" -- Ruutu "1"
	class Pelilauta{
	}
	class Ruutu{
	}
	class SeuraavaRuutu{
	}
