# BookBuddy

BookBuddy on ns. "virtuaalinen kirjahylly". Sovelluksen avulla on mahdollista pitää kirjaa luetuista, tällä hetkellä luettavista sekä vielä lukemattomista kirjoista. Sovellusta on mahdollista käyttää useampi käyttäjä, joilla kaikilla on omat kirjahyllynsä sekä kirjansa. Sovelluksen tarkempi kuvaus löytyy vaatimusmäärittelystä.

- [Lopullinen release (loppupalautus)](https://github.com/helinal/ot-harjoitustyo/releases/tag/final)
- [Toinen release (vko 6)](https://github.com/helinal/ot-harjoitustyo/releases/tag/viikko6)
- [Ensimmäinen release (vko 5)](https://github.com/helinal/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

- [Käyttöohje](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/testaus.md)
- [Työaikakirjanpito](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

## Asennus

Asenna ensin riippuvuudet komennolla

```bash
poetry install
```

Suorita sitten vaadittavat alustustoimenpiteet

```bash
poetry run invoke build
```

Lopuksi käynnistä sovellus komennolla

```bash
poetry run invoke start
```

## Sovelluksen komentorivitoiminnot

> Huom: Jos et joka komennon yhteydessä halua kirjoittaa `poetry run`, voit ennen komentojen suorittamista siirtyä virtuaaliympäristöön komennolla `poetry shell`


### Ohjelman käynnistys

Ohjelma käynnistyy komennolla

```bash
poetry run invoke start
```

### Testaus

Testit voi suorittaa komennolla

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportti generoituu komennolla

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon

### Pylint

Pylint-tarkastukset voi suorittaa komennolla

```bash
poetry run invoke lint
```
