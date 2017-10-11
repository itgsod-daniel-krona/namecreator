# namecreator program

Ett litet program som läser in användare, förnamn och efternam och utifrån detta skapar unika användarnamn.

Användarnamn läses in från en fil users.csv, resultatet sparas i en csvfil usernicks.csv i formen

    förnamn, efternamn, användarnamn

# användarnamn pseudokod

Läs in fulla namnet (ex: Daniel Mikael Åberg).
Om det fulla namnet har tre ord (___ ___ ___) så måste programmet komma ihåg det och uppfatta att användaren har ett
mellannamn.
Ändra å och ä till a och ö till o för att inte få något strul med texten (ex: Daniel Mikael Aberg).
Ändra stora bokstäver till små för att det ska bli enklare att både skriva in och hitta namnet när det är sparat
(ex: daniel mikael aberg).
Dela upp namnet till de 3 första bokstäverna (eventuellt första bokstaven i mellannamn) och de 3 första bokstäverna
i efternamnet för att skapa ett användarnamn
(ex: dan m abe).
Ta bort mellanrum för att det ska bli lättare att hitta och skriva in användarnamnet. (ex: danmabe).
Kolla igenom alla sparade användarnamn för att se om det är unikt. Om det är unikt så sparas användarnamnet i en
katalog som förvarar alla inloggningar.
Om användarnamnet inte är unikt så läggs en siffra från 0-9 till i slutet beroende på hur många likadana användarnamn
som är sparade (ex: danmabe0).
Användarnamnet sparas i en katalog med alla inloggningar med information som att användarnamnet: danmabe tillhör
användaren Daniel Mikael Aberg.
