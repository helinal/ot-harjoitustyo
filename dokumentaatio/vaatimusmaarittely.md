# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä pystyy pitämään kirjaa kirjoista, joita joko haluaisi lukea, on tällä hetkellä lukemassa tai on jo lukenut - ns. "virtuaalinen kirjahylly". Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä, joilla kaikilla on omat kirjalistansa.

## Käyttäjät

Kehityksen alkuvaiheessa vain yksi peruskäyttäjä-käyttäjärooli, kehityksen edetessä saatetaan lisätä ns. admin-käyttäjärooli.

## Sovelluksen tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi kirjautua sisään kirjautumislomakkeella
  - Jos käyttäjää ei ole olemassa tai salasana ei täsmää, ilmoittaa järjestelmä tästä
- Jos käyttäjällä ei ole vielä tunnusta, voi käyttäjä luoda uuden käyttäjätunnuksen
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä

### Kirjautumisen jälkeen

- Käyttäjä näkee etusivulla omat kirjalistansa:
  - kirjat, jotka käyttäjä haluaa lukea
  - kirjat, joita käyttäjä lukee tällä hetkellä
  - kirjat, jotka käyttäjä on jo lukenut
- Käyttäjä voi lisätä uuden kirjan johonkin kolmesta listasta
- Käyttäjä voi poistaa kirjan listasta
- Käyttäjä voi kirjautua ulos järjestelmästä

## Jatkokehitysideoita

- Kirjojen haku hakusanan, genren, kirjailijan jne. avulla
- Kirjalistan tai -listojen järjestely esim. tärkeysjärjestyksen mukaan
- Kirjan siirto listasta toiseen, esim. lukemassa -> luettu
- Jo luetun kirjan arvostelu ja kommentointi
- Käyttäjätunnusten poisto