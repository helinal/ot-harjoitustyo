# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä pystyy pitämään kirjaa kirjoista, joita joko haluaisi lukea, on tällä hetkellä lukemassa tai on jo lukenut - ns. "virtuaalinen kirjahylly". Sovellusta voi käyttää useampi rekisteröitynyt käyttäjä, joilla kaikilla on omat kirjalistansa.

## Käyttäjät

Kehityksen alkuvaiheessa vain yksi peruskäyttäjä-käyttäjärooli, kehityksen edetessä saatetaan lisätä ns. admin-käyttäjärooli.

## Sovelluksen tarjoama toiminnallisuus

### Ennen kirjautumista

- Käyttäjä voi kirjautua sisään kirjautumislomakkeella (**Tehty**)
  - Jos käyttäjää ei ole olemassa tai salasana ei täsmää, ilmoittaa järjestelmä tästä (**Tehty**)
- Jos käyttäjällä ei ole vielä tunnusta, voi käyttäjä luoda uuden käyttäjätunnuksen (**Tehty**)
  - Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä (**Tehty**)

### Kirjautumisen jälkeen

- Käyttäjä näkee etusivulla omat kirjalistansa: (**Tehty**)
  - kirjat, jotka käyttäjä haluaa lukea (**Tehty**)
  - kirjat, joita käyttäjä lukee tällä hetkellä (**Tehty**)
  - kirjat, jotka käyttäjä on jo lukenut (**Tehty**)
- Käyttäjä voi lisätä uuden kirjan johonkin kolmesta listasta (**Tehty**)
- Käyttäjä voi poistaa kirjan listasta
- Käyttäjä voi kirjautua ulos järjestelmästä (**Tehty**)

## Jatkokehitysideoita

- Kirjojen haku hakusanan, genren, kirjailijan jne. avulla
- Kirjalistan tai -listojen järjestely esim. tärkeysjärjestyksen mukaan
- Kirjan siirto listasta toiseen, esim. lukemassa -> luettu
- Jo luetun kirjan arvostelu ja kommentointi
- Käyttäjätunnusten poisto
