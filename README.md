# BajmBlog 2: Upadłe królestwo
Long awaited sequel

## Opis
Prosta gra rpg z całkiem znośną mechaniką, ale zdecydowanie zbyt małym budżetem. Zadaniem gracza jest zbieranie kolejnych utworów Bajmu walcząc jednocześnie z pojawiającymi się przeciwnikami.
Projekt kontynuowany po ocenie z nadzieją na prześcignięcie Fallouta 76 (co już chyba zostało osiągnięte).
Fabuła też będzie.

## Autorzy
Jakub Dakowski, Natalia Majda, Wojciech Zięba

## Instrukcja obsługi
### Uruchamianie:
   1. Potrzebne będą Ci moduły:
      - `tkinter`
      - `PIL`
      - `requests`
      - `BeautifulSoup`
      - `sqlite3` - instalowany poprzez zainstalowanie oprogramowania sqlite3
   2. Uruchom plik `menu.py`
   3. Warto w tym miejscu zaktualizować bazę cytatów. Opcję tą znajdziesz w zakładce "Opcje".
   4. Rozpocznij grę & enjoy!
### Tips and tricks:
   - __Możesz__ zmienić z czyimi utworami będziesz walczył. Wystarczy, że podasz link do strony zespołu pozbawiony `.html`. Na przykład: `https://www.tekstowo.pl/piosenki_artysty,liroy`. Po naciśnięciu przycisku program zaktualizuje tylko bazę przeciwnika bez zmian w zapisie Bajmu. Domyślnie wybierani są Bracia Golec
   - Zwracaj uwagę na konstrukcję utworu i ich zapisu na tekstowo.pl! Obrażenia zadawane przez linie są równe ilości znaków w cytacie, możesz dzięki znajomości tego oceniać jakie są szansę na poszczególne obrażenia!
   - EQ resetuje się tylko przy aktualizacji bazy cytatów. Co za tym idzie możesz walczyć ile chcesz, z kim chcesz i nie tracić ekwipunku. Złap je wszystkie!
