# Cvičení 6 – GitHub Actions (bonus)

**Cíl:** vidět v akci základní CI (Continuous Integration) – automatickou
kontrolu, která se spustí při každém push/PR.

Toto cvičení je bonusové – navazuje na předchozí, ale není nutné pro
pochopení základního git workflow.

## Co už v repu je

V [`.github/workflows/ci.yml`](../.github/workflows/ci.yml) je jednoduchý
workflow, který se spustí při každém push nebo PR na `main`:

1. nastaví Python,
2. nainstaluje závislosti z `requirements.txt`,
3. ověří, že se `scripts/analyza_prodeju.py` dá bez chyby importovat a
   spustit.

## Postup

1. Založte novou větev a do skriptu úmyslně vpravte chybu – např. překlep
   v názvu sloupce (`df["mnozstvi_TYPO"]`).

2. Commitněte, pushněte a otevřete PR.

3. V PR si všimněte záložky **Checks** – workflow se spustí automaticky a
   skončí červeně (❌). GitHub vám u PR ukáže, že kontrola neprošla.

4. Klikněte na detail failnutého checku a najděte v logu chybovou hlášku.

5. Opravte chybu, commitněte a pushněte znovu do stejné větve – workflow se
   spustí znovu a tentokrát by měl projít zeleně (✅).

6. Teprve zelený check mergujte do `main`.

## Na co se zaměřit

- CI negarantuje, že je kód *správně* – jen že prošel definovanými
  kontrolami (tady: že se dá spustit). Testy si stále musíte navrhnout
  sami.
- Zvyk "nemergovat na červeno" je základ týmové spolupráce – chrání
  ostatní před tím, že si stáhnou rozbitý `main`.

## To je vše

Tímto končí základní sada cvičení. Pro kontrolu očekávaného výsledku
jednotlivých kroků se podívejte do
[solutions/SOLUTIONS.md](../solutions/SOLUTIONS.md).
