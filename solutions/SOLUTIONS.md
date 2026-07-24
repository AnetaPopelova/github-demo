# Poznámky k řešení cvičení

Tento soubor slouží k sebekontrole (nebo pro lektora) – nejsou to hotové
diffy, ale popis, jak má vypadat výsledný stav po každém cvičení.

## 01 – první commit

- V `scripts/analyza_prodeju.py` přibyla funkce `prumerna_hodnota_objednavky`
  vracející `df["trzba"].mean()`, zavolaná a vypsaná v `main()`.
- Ve `main` branch (po pushi) je nový commit s výstižnou zprávou.

## 02 – branch a pull request

- Existuje větev `feature/trzba-podle-mesice` (nebo je již sloučená).
- Přibyla funkce `trzba_podle_mesice`, používající
  `df["datum"].dt.to_period("M")` a `groupby`.
- Na GitHubu existuje PR s popisem změny.

## 03 – code review

- PR z cvičení 2 má alespoň jeden review komentář a je sloučený metodou
  **Squash and merge**.
- Větev `feature/trzba-podle-mesice` je po sloučení smazaná (na GitHubu i
  lokálně).

## 04 – merge konflikt

- V historii `main` jsou dva samostatné PR měnící stejný řádek (hlavičku
  výpisu celkové tržby).
- Druhý PR obsahoval merge/rebase konflikt, který byl ručně vyřešen – v
  historii je vidět commit typu "Vyresit konflikt...".
- Finální podoba řádku kombinuje/rozhoduje mezi oběma variantami – žádné
  značky `<<<<<<<` v souboru nezůstaly.

## 05 – issues

- Na GitHubu existuje issue popisující chybný záznam v datech.
- `data/prodeje.csv` už neobsahuje řádek s "Prosle mleko".
- Issue je po sloučení PR automaticky uzavřené (díky `Fixes #cislo` v
  popisu PR).

## 06 – GitHub Actions (bonus)

- V historii PR je vidět alespoň jeden neúspěšný a jeden úspěšný běh
  workflow `CI` (záložka Actions).
- `main` obsahuje jen commit se zeleným (úspěšným) checkem.
