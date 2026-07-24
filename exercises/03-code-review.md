# Cvičení 3 – code review

**Cíl:** vyzkoušet si review Pull Requestu na GitHubu – ze strany autora i
reviewera.

Toto cvičení funguje nejlépe ve dvojici (recenzujete si PR navzájem). Pokud
cvičíte sami, projděte oba pohledy postupně.

## Jako reviewer

1. Otevřete PR z předchozího cvičení v záložce **Files changed**.
2. U konkrétních řádků přidejte komentáře – např.:
   - je název proměnné/funkce srozumitelný?
   - chybí nějaký edge case (prázdná data, chybějící sloupec)?
   - odpovídá commit message tomu, co se skutečně změnilo?
3. Rozhodněte se pro jeden z výstupů review:
   - **Comment** – jen poznámky, nic nebrání mergi,
   - **Approve** – změna je v pořádku,
   - **Request changes** – je potřeba něco upravit před mergem.

## Jako autor

1. Reagujte na komentáře – buď vysvětlete rozhodnutí, nebo změnu upravte.
2. Pokud jste dostali "Request changes", proveďte úpravu přímo ve stejné
   větvi:

   ```bash
   git add scripts/analyza_prodeju.py
   git commit -m "Reagovat na review: osetrit prazdna data"
   git push
   ```

   PR se automaticky aktualizuje – není potřeba zakládat nový.

3. Jakmile je PR schválený (Approve), sloučte ho tlačítkem **Merge pull
   request** na GitHubu. Všimněte si voleb:
   - *Create a merge commit*
   - *Squash and merge*
   - *Rebase and merge*

   Pro tento repo použijte **Squash and merge** – v `main` tak zůstane
   jeden přehledný commit místo historie drobných oprav.

4. Po sloučení smažte větev (GitHub to nabídne tlačítkem) a lokálně si
   stáhněte aktuální `main`:

   ```bash
   git checkout main
   git pull
   git branch -d feature/trzba-podle-mesice
   ```

## Na co se zaměřit

- Review není o kritice autora, ale o kvalitě kódu – formulujte komentáře
  jako otázky/návrhy ("Co takhle...", "Nemělo by se ošetřit...").
- Malé, zaměřené PR se recenzují mnohem rychleji než velké.

Pokračujte cvičením [04 – merge konflikt](04-merge-konflikt.md).
