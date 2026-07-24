# Cvičení 2 – branch a pull request

**Cíl:** naučit se pracovat s větvemi a otevřít svůj první Pull Request (PR)
na GitHubu.

## Postup

1. Ujistěte se, že jste na `main` a máte aktuální stav:

   ```bash
   git checkout main
   git pull
   ```

2. Vytvořte novou větev pro svou změnu:

   ```bash
   git checkout -b feature/trzba-podle-mesice
   ```

3. V [`scripts/analyza_prodeju.py`](../scripts/analyza_prodeju.py) přidejte
   funkci `trzba_podle_mesice(df)`, která seskupí `trzba` podle měsíce
   (`df["datum"].dt.to_period("M")`) a výsledek vypište v `main()`.

4. Commitněte změnu (klidně víc menších commitů, pokud dává smysl):

   ```bash
   git add scripts/analyza_prodeju.py
   git commit -m "Pridat trzbu podle mesice"
   ```

5. Pushněte větev na GitHub:

   ```bash
   git push -u origin feature/trzba-podle-mesice
   ```

6. Na GitHubu otevřete **Pull Request** z `feature/trzba-podle-mesice` do
   `main`. Do popisu PR napište:
   - co změna dělá,
   - jak jste ji otestovali (spustili jste skript?).

7. Zatím PR nemergujte – budeme ho potřebovat v dalším cvičení pro code
   review.

## Na co se zaměřit

- Název větve by měl napovídat, o co jde (`feature/...`, `fix/...`).
- Jeden PR = jedna logická změna. Nesnažte se do jednoho PR nacpat víc
  nesouvisejících věcí.
- Popis PR čte reviewer, který nemusí znát kontext – piště tak, aby dával
  smysl i bez vás.

Pokračujte cvičením [03 – code review](03-code-review.md).
