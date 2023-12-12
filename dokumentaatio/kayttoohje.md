# Käyttöohje

## Ohjelman käynnistäminen

Asenna ensin ohjelman riippuvuuden komennolla

```bash
poetry install
```

Suorita sitten tarvittavat alustustoimenpiteet komennolla

```bash
poetry run invoke build
```

Nyt voit käynnistää ohjelman komennolla

```
poetry run invoke start
```

## Kirjautuminen sisään

Kun käynnistät sovelluksen, käynnistyy sovellus kirjautumisnäkymään.
Kirjautuminen onnistuu kirjoittamalla (olemassaoleva) käyttäjätunnus ja salasana kenttiin ja painamalla _Login_-nappia.

## Uuden käyttäjän luominen

Kirjautumisnäkymästä pääsee rekisteröimään uuden käyttäjän painamalla _Create user_-nappia.
Luo uusi käyttäjä syöttämällä uusi käyttäjätunnus ja salasana syötekenttiin ja painamalla _Create a new user_-nappia.
Jos käyttäjän luominen onnistuu, sovellus kirjautuu automaattisesti sisään uusilla tunnuksilla ja siirtyy sovelluksen 'pääsivulle'.

## Uuden kirjan lisääminen kirjahyllyyn

Kirjautunut käyttäjä voi lisätä uuden kirjan yhteen kolmesta kirjahyllystä syöttämällä kirjan otsikon syötekenttään,
valitsemalla valikosta yhden kolmesta kirjahyllystä ja painamalla _Add a new book_-nappia.

## Kirjan poistaminen kirjahyllystä

Jo lisätyn kirjan voi poistaa kirjahyllystä yksinkertaisesti painamalla _Delete_-nappia sen kirjan vierestä, jonka käyttäjä haluaa poistaa.

## Kirjautuminen ulos

Kirjautunut käyttäjä voi kirjautua ulos painamalla _Logout_-nappia, jolloin käyttäjä kirjataan ulos ja sovellus palaa takaisin kirjautumisnäkymään.
