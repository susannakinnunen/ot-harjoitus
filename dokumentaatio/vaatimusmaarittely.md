# Vaatimusmäärittely

## Sovelluksen tarkoitus

Kyseessä on venyttelysovellus. Käyttäjä pääsee hakemaan kehonosakohtaisia venyttelyohjeita. Ylläpitäjä vastaa kehonosien ja venytysohjeiden lisäämisestä.

## Käyttäjät
Normaalikäyttäjät pääsevät näkemään venyttelyohjeet.

Ylläpitäjä voi lisätä kehonosia ja venyttelyohjeita.

## Käyttöliittymäluonnos tekstimuodossa

1. Aloitusnäkymä, josta voi siirtyä rekisteröitymään tai kirjautumaan sisään.
2. Rekisteröitymisnäkymä.
3. Kirjautumisnäkymä.
4. (Normikäyttäjä) Lista kehonosista, hakukenttä venytyksille, kirjaudu ulos -painike.
5. (Ylläpitäjä) Lista kehonosista, hakukenttä venytyksille, kirjaudu ulos -painike, ylläpitäjän toiminnallisuudet painike.
6. (Normikäyttäjä) Lista venytyksistä tietylle kehonosalle, josta pääsee takaisin 4. näkymään.
7. (Ylläpitäjä) Lista venytyksistä tietylle kehonosalle, josta pääsee takaisin 5.näkymään.
8. (Ylläpitäjä) Venytyksen lisäämismahdollisuus.

## Perusversion tarjoama toiminnallisuus

**Ennen kirjautumista**
- Käyttäjä voi luoda itselleen tunnuksen 
	- Käyttäjätunnus on uniikki ja sen pituus on vähintään 3 merkkiä.
- Käyttäjä voi kirjautua sisään, jos hänellä on olemassa oleva tunnus järjestelmään 
	- Järjestelmä ilmoittaa, jos käyttäjätunnusta ei löydy tai jos salasana ei täsmää.
	

**Kirjautumisen jälkeen**
- Kirjautumisen jälkeen käyttäjä näkee listan kehonosista
	-  kirjoittamalla listassa annetun kehonosan, käyttäjä pääsee näkemään siihen sopivan venyttelyohjeen 

- Ylläpitäjä pystyy myös:
	-  lisäämään kehonosia ja venyttelyohjeita.


## Jatkokehitysideoita
- Siistimpi käyttöliittymä
- Ylläpitäjä pystyy poistamaan ja muokkaamaan venyttelyohjeita
- Käyttäjä voi ehdottaa ylläpidolle kehonosia, joille kaipaisi venyttelyohjetta
- Käyttäjä voi merkitä ylös lempivenyttelynsä
- Venyttelyohjeeseen tulee mahdollisesti myös kuva
