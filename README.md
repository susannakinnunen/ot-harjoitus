# Venyttelysovellus

Venyttelysovelluksen tarkoituksena on olla sovellus, josta voi etsiä kehonosakohtaisia venyttelyohjeita.
Käyttäjän tulee ensin rekisteröityä ja kirjautua sisään, ennen kuin pääsee näkemään venyttelyohjeita.

## Dokumentaatio

- [changelog](https://github.com/susannakinnunen/ot-harjoitus/blob/master/dokumentaatio/changelog.md)

- [työaikakirjanpito](https://github.com/susannakinnunen/ot-harjoitus/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [vaatimusmäärittely](https://github.com/susannakinnunen/ot-harjoitus/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [arkkitehtuuri.md](https://github.com/susannakinnunen/ot-harjoitus/blob/master/dokumentaatio/arkkitehtuuri.md)

- [release](https://github.com/susannakinnunen/ot-harjoitus/releases)

## Komentorivitoiminnot 

**Ohjelman suorittaminen**

Sovelluksen suorituksessa tarvitaan bodyparts.csv- ja stretches.csv tiedostot. Niille tulee tehdä ympäristönmuuttujat .src/.env-tiedostoon:
bodypart_file = bodyparts.csv
stretch_file = stretches.csv

.csv-tiedostoissa ei tarvitse olla mitään ennen ohjelman aloittamista. Jos niissä on jotakin, niin se ei kuitenkaan haittaa, sillä ohjelma tyhjentää tiedostot ennen tekstikäyttöliittymän käynnistymistä.

Tällä hetkellä (26.4.) käyttäjän täytyy joka kerta rekisteröityä uudestaan eli samalla käyttäjätunnuksella ei voi kirjautua sisään, kun käynnistää ohjelman uudelleen.

Ohjelman pystyy suorittamaan komennolla:
```
poetry run invoke start
```
**Testaus**

Testit voi suorittaa komennolla:
```
poetry run invoke test
```

Testikattavuusraportin voi generoida komennolla:
```
poetry run invoke coverage-report
```
**Pylint**

Pylint-laatutarkastuksen tulokset saa näkyviin komennolla:
```
poetry run invoke lint
```
**Automaattinen formatointi**

PEP 8 -tyyliohjeiden mukainen automaattinen formatointi toimii komennolla:
```
poetry run invoke format
```
