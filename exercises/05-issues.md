# Cvičení 5 – issues

**Cíl:** naučit se používat GitHub Issues pro sledování práce a propojit je
s Pull Requesty.

## Postup

1. Na GitHubu v repu otevřete záložku **Issues** -> **New issue**.

2. Založte issue popisující chybu v datech: v
   [`data/prodeje.csv`](../data/prodeje.csv) je řádek
   `2026-01-14,Prosle mleko,Potraviny,Brno,20,24`, který zkresluje analýzu
   (jde o testovací/chybný záznam, ne o skutečný prodej). Do issue napište:
   - **Popis:** jaký je problém a kde se projevuje,
   - **Očekávané chování:** co by mělo být výsledkem po opravě,
   - **Kroky k reprodukci:** jak si to ověřit (spustit
     `scripts/analyza_prodeju.py` a podívat se na kategorii Potraviny).

3. Všimněte si čísla issue (např. `#3`) – budete ho potřebovat.

4. Založte novou větev a proveďte opravu (odstraňte/opravte daný řádek v
   `data/prodeje.csv`):

   ```bash
   git checkout main
   git pull
   git checkout -b fix/chybny-zaznam-mleko
   ```

5. Commitněte se zmínkou čísla issue:

   ```bash
   git add data/prodeje.csv
   git commit -m "Odstranit chybny testovaci zaznam z dat (#3)"
   git push -u origin fix/chybny-zaznam-mleko
   ```

6. Otevřete PR a do popisu napište `Fixes #3` (nebo `Closes #3`). GitHub
   pak po sloučení PR **automaticky uzavře** propojené issue.

7. Po review a merge zkontrolujte, že se issue skutečně samo zavřelo.

## Na co se zaměřit

- Issues nejsou jen pro bugy – hodí se i na návrhy vylepšení, otázky nebo
  rozdělení větší práce na menší kroky (tzv. tasky).
- Klíčová slova `Fixes`/`Closes`/`Resolves` + číslo issue v popisu PR nebo
  v commit message vytvoří automatické propojení – šetří to ruční práci a
  udržuje historii přehlednou.

Pokračujte cvičením [06 – GitHub Actions (bonus)](06-github-actions.md).
