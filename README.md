# VideoGenerator

Cílem je automaticky vytvářet krátká videa ve formátu 9:16 o statistikách v Evropě. Video bude obsahovat mapu, porovnání zemí, hudbu a případně komentář.

## Technologie

- **Python** – zpracování dat, scénář a grafické prvky.
- **FFmpeg** – sestavení výsledného videa, hudba a titulky.
- **SVG** – mapa Evropy a popisky států.
- **LLM / AI API** – generování scénáře ve formátu JSON (např. Groq, případně placené ChatGPT).
- **GitHub** – uložení a sdílení kódu.
- **GitHub Actions** – automatické spouštění.
- **E-mail** – schvalování videí.


### Verze 1

- AI vytvoří scénář ve formátu JSON: otázku, odpovědi a porovnání evropských zemí.
- Python přiřadí hodnoty státům na mapě Evropy ve formátu SVG.
- Upravení velikosti textu a obarvení zemí podle výsledků.
- Přidání pozadí a hudby, následně sestavení videa přes FFmpeg.
- Každé video nejprve ručně schválíme.
- Cíl: připravovat 3 videa denně, přibližně po 8 hodinách.

### Verze 2

- Vyhodnocování statistik videí z YouTube, Instagramu a TikToku.
- Podle výsledků upravovat vybrané části promptu.
- AI bude smět měnit pouze předem určené části promptu.

### Verze 3

- PNG postavička v různých stylech, která vypráví informace ve videu.
- Scénář včetně časování a reakcí postavičky.
- Generování hlasu přes ElevenLabs.
- Automatické titulky pomocí FFmpeg.
- Zvýraznění a přibližování právě probíraných zemí.
- Případné doplnění dalších obrázků a zvuků.

## Schvalování

- Po vygenerování videa se odešle e-mail s odkazem.
- Možnosti: **schválit**, **zamítnout**, **vygenerovat další**.
- Podle odpovědi se automaticky spustí další krok.
- E-mail bude sloužit jako jednoduché rozhraní, není potřeba vytvářet vlastní aplikaci.

## Provoz

- Kód bude uložený na GitHubu.
- Generování poběží na GitHub-hosted runneru `ubuntu-latest`.
- GitHub Actions bude spouštět generování automaticky 3× denně pomocí cron plánovače.
- Nebude potřeba mít zapnutý vlastní počítač.
- Runner automaticky nainstaluje Python, potřebné knihovny a FFmpeg.
- Python připraví scénář, mapu a další prvky; FFmpeg z nich vytvoří video.
- Hotové video se uloží mezi GitHub Actions Artifacts, odkud si ho budeme moci stáhnout.
- Artefakty budou uchovávány po omezenou dobu, například 7 dní.
- Pokud bezplatné možnosti AI nebudou stačit, můžeme přejít na placené řešení.

### GitHub Free

- Soukromý repozitář má v rámci GitHub Free limit 2 000 minut GitHub Actions měsíčně.
- Při třech videích denně počítáme přibližně s 90 běhy za měsíc.
- To vychází na průměrně 22 minut na jeden běh.
- Do času se započítává instalace závislostí i samotné generování videa.
- Pokud jeden běh trvá 15 minut, spotřebujeme přibližně 1 350 minut měsíčně.
- Pokud jeden běh trvá 20 minut, spotřebujeme přibližně 1 800 minut měsíčně.
- Pokud jeden běh trvá 25 minut, překročíme měsíční limit.
- GitHub Free by tedy mohl stačit, pokud se průměrná doba běhu vejde do dostupného limitu.
- Kromě toho je potřeba sledovat velikost uložených artefaktů.
