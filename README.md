# Git & GitHub pro datové analytiky – demo repo

Toto repo slouží jako cvičební sandbox pro juniorní datové analytiky se
základy Pythonu, kteří se poprvé seznamují s **gitem a GitHubem**.

Neřešíme tu pokročilou analytiku – kód je záměrně jednoduchý (pandas nad
jedním CSV souborem). Cílem je nacvičit si běžný git/GitHub workflow na
něčem, co jako datový analytik reálně uvidíte.

## Co se naučíte

- základní git cyklus: `add` → `commit` → `push` → `pull`
- práci s větvemi (branch) a Pull Requesty
- code review na GitHubu
- řešení merge konfliktů
- issues a propojení s PR
- (bonus) základní CI přes GitHub Actions

## Instalace

```bash
python -m venv venv
source venv/bin/activate      # na Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Ověřte, že skript funguje:

```bash
python scripts/analyza_prodeju.py
```

## Struktura repa

```
data/                 ukázková data (prodeje.csv)
scripts/              jednoduchý analytický skript
exercises/            cvičení, projděte v pořadí 01 -> 06
solutions/            poznámky, jak má vypadat výsledek cvičení
.github/workflows/    ukázkový CI workflow (bonus cvičení 06)
```

## Jak postupovat

Nemáte ještě GitHub účet nebo VS Code propojené s gitem? Začněte cvičením
[exercises/00-registrace-a-nastaveni.md](exercises/00-registrace-a-nastaveni.md).

Jinak rovnou otevřete
[exercises/01-prvni-commit.md](exercises/01-prvni-commit.md) a pokračujte
v pořadí. Každé cvičení staví na tom předchozím.
