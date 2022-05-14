# Venyttelysovellus

Venyttelysovelluksessa käyttäjä voi etsiä kehonosakohtaisia venyttelyohjeita.
Käyttäjän tulee ensin rekisteröityä ja kirjautua sisään, ennen kuin pääsee näkemään venyttelyohjeita.

Ylläpitäjä pystyy lisäämään kehonosia ja venyttelyohjeita. Voit koittaa ylläpitäjän toimintoja luomalla "admin"-nimisen käyttäjätunnuksen.

## Dokumentaatio

- [changelog](https://github.com/susannakinnunen/ot-harjoitus/blob/master/dokumentaatio/changelog.md)

- [työaikakirjanpito](https://github.com/susannakinnunen/ot-harjoitus/blob/master/dokumentaatio/tyoaikakirjanpito.md)

- [vaatimusmäärittely](https://github.com/susannakinnunen/ot-harjoitus/blob/master/dokumentaatio/vaatimusmaarittely.md)

- [arkkitehtuuri.md](https://github.com/susannakinnunen/ot-harjoitus/blob/master/dokumentaatio/arkkitehtuuri.md)

- [release](https://github.com/susannakinnunen/ot-harjoitus/releases)

## Komentorivitoiminnot 

**Ohjelman suorittaminen**

Toistaiseksi käyttäjän täytyy joka kerta rekisteröityä uudestaan eli samalla käyttäjätunnuksella ei voi kirjautua sisään, kun käynnistää ohjelman uudelleen.

Jos haluat koittaa ylläpitäjän oikeuksia, luo uusi käyttäjätunnus nimellä 'admin' ja kirjaudu sillä sisään. 

.csv-tiedostoissa ei tarvitse olla mitään ennen ohjelman aloittamista. Jos niissä on jotakin, niin se ei kuitenkaan haittaa, sillä ohjelma tyhjentää tiedostot ennen tekstikäyttöliittymän käynnistymistä.

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
