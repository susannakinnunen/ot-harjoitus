```mermaid
classDiagram
	Pelilauta "40" -- "1" Ruutu
	Ruutu --|> SeuraavaRuutu
	Pelinappula "*" -- "1" Ruutu
	class Pelilauta{
	}
	class Ruutu{
	}
	class SeuraavaRuutu{
	}
