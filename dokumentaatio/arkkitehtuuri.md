# Arkkitehtuurikuvaus

## Sovelluslogiikka luokkakaaviona

Sovelluksessa on luokat User, Book sekä Bookshelf. Alla oleva luokkakaavio kuvaa luokkien välisiä yhteyksiä:

```mermaid
 classDiagram
      User "1" --> "*" Book
      Book "*" --> "1" Bookshelf
      class User{
          username
          password
      }
      class Book{
          id
          title
          author
          genre
          year
          pages
      }
      class Bookshelf{
          name
          books
      }
 
```

## Päätoiminnallisuudet

### Käyttäjän kirjautuminen

Kun käyttäjä syöttää kenttiin käyttäjätunnuksen ja salasanan sekä painaa nappia _Login_, kirjataan käyttäjä sisään. Seuraava sekvenssikaavio kuvaa tarkemmin kirjautumista:

```mermaid
sequenceDiagram
  actor User
  participant UI
  participant BookService
  participant UserRepository
  User->>UI: click "Login" button
  UI->>BookService: login("nallepuh", "nalle321")
  BookService->>UserRepository: find_by_username("nallepuh")
  UserRepository-->>BookService: user
  BookService-->>UI: user
  UI->UI: show_books_view()
```

Sekvenssikaaviot sovelluksen muista toiminnallisuuksista lisätään piakkoin.
