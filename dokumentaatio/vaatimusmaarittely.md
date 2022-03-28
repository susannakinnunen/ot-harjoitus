# Vaatimusmäärittely

## Sovelluksen tarkoitus

Kyseessä on venyttelysovellus. Käyttäjä näkee listan kehonosista ja klikkaamalla kehonosaa saa siihen sopivia venyttelyohjeita. (Huom. aihe on muuttunut sitten viime viikon palautuksen)

## Käyttäjät
Normaalikäyttäjät pääsevät näkemään venyttelyohjeet.

Ylläpitäjä voi lisätä, muokata ja poistaa kehonosia ja venyttelyohjeita.

## Käyttöliittymäluonnos tekstimuodossa

Käyttöliittymä koostuu noin. 6 eri näkymästä:

1. Kirjautuminen   <---Jos ei tunnusta--->  2. Tunnuksen luominen
3. Lista kehonosista 4. Lista valitulle kehonosalle sopivia venyttelyohjeita

Ylläpitäjälle näkyvä sivu:
5. Näkymä 3, jossa myös mahdollisuus lisätä uusi kehonosa
6. Näkymä 4, jossa myös mahdollisuus lisätä uusi venyttelyohje

## Perusversion tarjoama toiminnallisuus

**Ennen kirjautumista**
- Käyttäjä voi luoda itselleen tunnuksen
	- Käyttäjätunnus on uniikki ja sen pituus on vähintään 3 merkkiä.
- Käyttäjä voi kirjautua sisään, jos hänellä on olemassa oleva tunnus järjestelmään
	- Järjestelmä ilmoittaa, jos käyttäjätunnusta ei löydy tai jos salasana ei täsmää.
	

**Kirjautumisen jälkeen**
- Kirjautumisen jälkeen käyttäjä näkee listan kehonosista, joita klikkaamalla hän pääsee näkemään sopivat venyttelyohjeet.

- Ylläpitäjä pystyy myös lisäämään, muokkaamaan ja poistamaan kehonosia ja venyttelyohjeita.


## Jatkokehitysideoita

- Käyttäjä voi ehdottaa ylläpidolle kehonosia, joille kaipaisi venyttelyohjetta
- Käyttäjä voi etsiä venyttelyohjeita hakukentästä
- Käyttäjä voi merkitä ylös lempivenyttelynsä
- Venyttelyohjeeseen tulee mahdollisesti myös kuva
