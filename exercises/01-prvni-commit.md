# Cvičení 1 – první commit

**Cíl:** projít si základní cyklus `add -> commit -> push`.

Předpokladem je GitHub účet a naklonované repo ve VS Code – pokud to ještě
nemáte hotové, vraťte se ke cvičení
[00 – účet na GitHubu a nastavení VS Code](00-registrace-a-nastaveni.md).

## Postup

1. Otevřete naklonované repo ve VS Code a v integrovaném terminálu
   (`` Ctrl+` ``) ověřte, že jste ve správné složce a na větvi `main`:

   ```bash
   git status
   ```

2. Vytvořte a aktivujte virtuální prostředí, nainstalujte závislosti a
   ověřte, že skript běží (viz [README.md](../README.md)).

3. Otevřete [`scripts/analyza_prodeju.py`](../scripts/analyza_prodeju.py) a
   přidejte novou funkci `prumerna_hodnota_objednavky(df)`, která vrátí
   průměrnou hodnotu jednoho řádku (`trzba`) v datech. Zavolejte ji v
   `main()` a vypište výsledek.

4. Zkontrolujte, co se změnilo:

   ```bash
   git status
   git diff
   ```

5. Změnu přidejte do stage a commitněte s výstižnou zprávou:

   ```bash
   git add scripts/analyza_prodeju.py
   git commit -m "Pridat vypocet prumerne hodnoty objednavky"
   ```

6. Pushněte změnu na GitHub:

   ```bash
   git push
   ```

## Na co se zaměřit

- Commit message by měl vysvětlovat **co** a stručně **proč**, ne "update".
- `git status` a `git diff` používejte před každým commitem – nikdy
  necommitujte "naslepo".
- Nezapomeňte, že `git add` přidává do stage jen to, co explicitně
  vyjmenujete (nebo `.` pro vše) – zkontrolujte, že jste neposlali nic
  navíc (např. `venv/`).

Pokračujte cvičením [02 – branch a pull request](02-branch-a-pull-request.md).
