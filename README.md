
Snake Gra PL Super Chomikuj.pl – Dokumentacja

===========================
1. Plik: main.py (logika gry)
===========================
- Tworzy ekran gry (600x600, czarne tło)
- Ustawia sterowanie strzałkami
- Obsługuje pętlę gry (game_loop) oraz restart (restart_game)

Funkcje:
- game_loop(): sprawdza kolizje, porusza wężem, aktualizuje wynik
- restart_game(): resetuje stan gry i uruchamia ponownie pętlę

=============================
2. Plik: snake.py (klasa Snake)
=============================
- Reprezentuje węża jako listę segmentów (kwadratów)
- Główna funkcjonalność: poruszanie, rozszerzanie, reset

Metody:
- create_snake(): tworzy początkowego węża
- move(): przesuwa węża do przodu
- extend(): dodaje segment ogona
- up(), down(), left(), right(): zmiana kierunku ruchu
- reset_position(): ukrywa starego węża i tworzy nowego

=============================
3. Plik: food.py (klasa Food)
=============================
- Tworzy małe zielone jedzenie w losowym miejscu

Metody:
- refresh(): zmienia pozycję jedzenia na losową

===================================
4. Plik: scoreborde.py (Scorebord)
===================================
- Pokazuje wynik i komunikaty

Metody:
- update_score(): aktualizuje wynik
- increase_score(): zwiększa wynik o 1
- game_over(): pokazuje napis "GAME OVER"
- reset_score(): resetuje wynik i ekran

==================
Sterowanie:
==================
- Strzałki góra/dół/lewo/prawo – ruch węża
- R – restart gry

==================
Sugestie na przyszłość:
==================
- Dodanie poziomów trudności
- Bonusowe jedzenie, punkty życia
- Zapis najlepszych wyników do pliku
