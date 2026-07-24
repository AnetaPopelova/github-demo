# Cvičení 4 – merge konflikt

**Cíl:** zažít merge konflikt v bezpečném prostředí a naučit se ho vyřešit.
Toto je typicky nejvíc obávaná situace pro začátečníky – cílem cvičení je
ukázat, že je to jen běžná (a zvládnutelná) součást práce.

Konflikt si tentokrát sami vyrobíte – tak, aby dvě větve upravovaly stejný
řádek souboru odlišně.

## Postup

1. Ujistěte se, že jste na aktuálním `main`:

   ```bash
   git checkout main
   git pull
   ```

2. Založte první větev a upravte hlavičku výpisu v
   [`scripts/analyza_prodeju.py`](../scripts/analyza_prodeju.py) – řádek
   `print(f"Celkova trzba: {celkova_trzba(df):,.0f} Kc")` změňte např. na:

   ```python
   print(f"CELKOVA TRZBA: {celkova_trzba(df):,.0f} Kc")
   ```

   Commitněte, pushněte a přes GitHub PR sloučte do `main` (viz cvičení 2–3).

3. Vraťte se na `main` *před* pullem nejnovější změny a založte **druhou**
   větev ze staršího stavu (abyste konflikt garantovaně dostali):

   ```bash
   git checkout main
   git checkout -b feature/emoji-vypis
   ```

   Upravte **stejný řádek** jinak, např.:

   ```python
   print(f"💰 Celkova trzba: {celkova_trzba(df):,.0f} Kc")
   ```

   Commitněte a pushněte tuto větev.

4. Otevřete pro ni PR do `main`. GitHub nahlásí, že větev nejde sloučit
   automaticky – **This branch has conflicts that must be resolved**.

5. Konflikt vyřešte lokálně:

   ```bash
   git checkout feature/emoji-vypis
   git pull origin main
   ```

   Git vám v souboru označí konfliktní místo:

   ```
   <<<<<<< HEAD
   print(f"💰 Celkova trzba: {celkova_trzba(df):,.0f} Kc")
   =======
   print(f"CELKOVA TRZBA: {celkova_trzba(df):,.0f} Kc")
   >>>>>>> main
   ```

6. Ručně rozhodněte, jak má výsledek vypadat (třeba spojte obě varianty),
   odstraňte značky `<<<<<<<`, `=======`, `>>>>>>>` a soubor uložte.

7. Označte konflikt jako vyřešený a dokončete merge:

   ```bash
   git add scripts/analyza_prodeju.py
   git commit -m "Vyresit konflikt ve formatu vypisu trzby"
   git push
   ```

8. Vraťte se na GitHub – PR by teď měl jít bez problémů sloučit.

## Na co se zaměřit

- Konflikt neznamená, že jste udělali chybu – znamená, že git nedokáže
  sám rozhodnout, kterou verzi chcete. Rozhoduje vždy člověk.
- Před řešením konfliktu si vždy přečtěte obě strany (`HEAD` = vaše větev,
  `main` = druhá strana) a rozmyslete si výsledný stav – nekopírujte
  nazdařbůh.
- Po vyřešení vždy soubor znovu spusťte/otestujte – git vám neověří, že
  výsledný kód dává smysl.

Pokračujte cvičením [05 – issues](05-issues.md).
