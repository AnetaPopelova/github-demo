# Cvičení 0 – účet na GitHubu a nastavení VS Code

**Cíl:** mít funkční GitHub účet a propojené VS Code, abyste mohli rovnou
pokračovat cvičením [01 – první commit](01-prvni-commit.md).

Pokud už GitHub účet máte a VS Code používáte s gitem běžně, toto cvičení
přeskočte.

## 1. Založení GitHub účtu

1. Jděte na [github.com/signup](https://github.com/signup).
2. Zadejte e-mail, heslo a uživatelské jméno (bude vidět ve všech vašich
   repozitářích a commitech – zvolte profesionálně vyznívající jméno).
3. Ověřte e-mailovou adresu podle instrukcí, které vám GitHub pošle.
4. V nastavení účtu (**Settings -> Password and authentication**) zapněte
   **dvoufaktorové ověření (2FA)** – GitHub ho dnes pro řadu akcí
   vyžaduje a je to základní bezpečnostní hygiena.

## 2. Instalace Gitu a VS Code

1. Nainstalujte Git: [git-scm.com/downloads](https://git-scm.com/downloads)
   (na macOS lze také přes `xcode-select --install` nebo `brew install git`).
2. Nainstalujte VS Code: [code.visualstudio.com](https://code.visualstudio.com).
3. Ověřte instalaci gitu v terminálu:

   ```bash
   git --version
   ```

4. Nastavte svou identitu (použije se v commitech) – ideálně stejné jméno
   a e-mail, jaké máte na GitHubu:

   ```bash
   git config --global user.name "Vase Jmeno"
   git config --global user.email "vas@email.cz"
   ```

## 3. Přihlášení do GitHubu přímo z VS Code

1. Otevřete VS Code a vlevo dole klikněte na ikonu účtu (postavička) ->
   **Sign in with GitHub to use GitHub Copilot** / **Sign in to
   GitHub**. Pokud ikonu nevidíte, otevřete **Command Palette**
   (`Cmd+Shift+P`) a napište `GitHub: Sign in`.
2. VS Code otevře prohlížeč – přihlaste se svým GitHub účtem a potvrďte
   autorizaci (**Authorize Visual Studio Code**).
3. Vraťte se do VS Code – v levém dolním rohu by nyní mělo být vidět vaše
   GitHub uživatelské jméno.
4. V záložce **Extensions** (`Cmd+Shift+X`) si nainstalujte rozšíření
   **GitHub Pull Requests and Issues** – umožní vám později vytvářet a
   recenzovat PR přímo z VS Code, ne jen v prohlížeči.

## 4. Naklonování tohoto repozitáře přes VS Code

1. Otevřete Command Palette (`Cmd+Shift+P`) a napište `Git: Clone`.
2. Vyberte **Clone from GitHub** – protože jste přihlášení, VS Code vám
   nabídne vaše repozitáře k výběru (nebo vložte URL ručně).
3. Vyberte cílovou složku na disku a po dokončení klonování zvolte
   **Open** – VS Code otevře repo jako pracovní prostor.
4. V dolní liště VS Code by se mělo zobrazit jméno aktuální větve
   (`main`) – znamená to, že je repo správně rozpoznané jako git
   repozitář.
5. Otevřete integrovaný terminál (**Terminal -> New Terminal** nebo
   `` Ctrl+` ``) a ověřte:

   ```bash
   git remote -v
   git status
   ```

## Na co se zaměřit

- Uživatelské jméno a e-mail v `git config` se propisují do každého
  commitu natrvalo – jednou zvolené jméno je vidět i zpětně v historii.
- Přihlášení ve VS Code řeší autentizaci vůči GitHubu (push/pull, PR) –
  nemusíte si už ručně řešit hesla ani tokeny při každé operaci.
- Panel **Source Control** (ikona vpravo v levém sloupci, `Ctrl+Shift+G`)
  je grafická alternativa k `git status` / `git add` / `git commit` –
  klidně ho použijte místo terminálu, výsledek je stejný.

Pokračujte cvičením [01 – první commit](01-prvni-commit.md).
