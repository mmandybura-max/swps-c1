## Biblioteczka

Moja aplikacja będzie służyła do zarządzania moją domową biblioteczką.

* Chcę robić notatki o autorach (dodatkowe informacje), książkach (treść,
  czy się podobała itp.), wypożyczających (np. czy są terminowi) oraz
  wypożyczeniach (np. stan zwróconej książki).
* Wypożyczenia (moich) książek będą odnotowywane z datami wypożyczenia
i zwrotu. Dzięki temu będę wiedziała, kto wypożyczył którą książkę i czy
ją oddał.
* Książka może być na liście życzeń oraz w różnym stopniu przeczytania:
przed, w trakcie i po przeczytaniu.
* Chcę śledzić stan zużycia książki: po zwrocie chcę go aktualizować.
* Książki mogą mieć różnych właścicieli, w szczególności ja mogę np.
  pożyczyć książkę od koleżanki

### Modele danych

#### `Book` (Książka)

* Identyfikator [klucz] \
  `id: number`
* Autor \
  `author: Author`
* Tytuł \
  `title: string`
* ISBN \
  `isbn: string`
* Jakość:\
  `quality: number` (1-10)
* Właściciel: \
  `owner: Person`
* Stan (chciane, do przeczytania, w trakcie, przeczytana):\
  `status: wished, planned, in-progress, complete`
* Notatki \
  `notes: string` (optional)

#### `Author` (Autor)
* Identyfikator [klucz] \
  `id: number`
* Imię \
  `name: string`
* Nazwisko \
  `surname: string`
* Adres \
  `url: URL` (optional)
* Notatki \
  `notes: string` (optional) 

#### `Person` (Osoba)
* Identyfikator [klucz] \
  `id: number`
* Imię \
  `first_name: string`
* Nazwisko \
  `last_name: string`
* Numer telefonu \
  `phone: string` (optional)
* Notatki \
  `notes: string` (optional) 

#### `Lease` (Wypożyczenie)
* Książka \
  `book: Book`
* Posiadacz \
  `holder: Person`
* Data wypożyczenia \
  `lease_date: date`
* Data zwrotu \
  `return_date: date` (optional)
* Jakość wypożyczenia \
  `lease_quality: number` (1-10)
* Jakość zwrotu \
  `return_quality: number` (1-10)
* Notatki \
  `notes: string` (optional)
