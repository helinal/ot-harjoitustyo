# Ohjelmistotekniikka, harjoitustyö

> Sovelluksen etusivun ulkonäkö on vielä työn alla - lopullinen sovelluksen etusivu tulee siis toivon mukaan olemaan käytettävyyden ja ulkonäön puolesta huomattavasti parempi

Sovellus on ns. "virtuaalinen kirjahylly". Sovelluksen avulla siis on mahdollista pitää kirjaa luetuista, tällä hetkellä luettavista sekä vielä lukemattomista kirjoista. Sovellusta on mahdollista käyttää useampi käyttäjä, joilla kaikilla on omat kirjahyllynsä sekä kirjansa. Tarkempi kuvaus löytyy vaatimusmäärittelystä.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](https://github.com/helinal/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Asennus

Asenna ensin riippuvuudet komennolla

```bash
poetry install
```

Suorita sitten vaadittavat alustustoimenpiteet

```bash
poetry run invoke build
```

Lopuksi,käynnistä sovellus komennolla

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
