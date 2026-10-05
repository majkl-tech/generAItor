Verze 1
groq llama-3.3-70b / později GPT-4o-mini 
FFmpeg 
Python

Pozadí a hudba stažená
Zkusit udelat UI pres github pomoci “issue”

Cíl → vytvořit 9:16, velmi krátké video o nějaké statistice v Evropě
s hudbou a pozadím, viz obrázek

LLM vytvoří do JSON formátu skript 
skript = (premise, odpoví na otázku, srovná země)
programem přiřadíme odpovědi k zemím evropy na svg formátu,
budeme muset také upravit velikost textu,
dáme jim barvy podle porovnání, přidáme pozadí, hudbu

Každé video bude muset projít schválením kvality od nás
Videa se budou automaticky uploadovat 3 krát denně po 8 h

Verze 2
self learning - ze statistik yt, ig, a tt
po několika dnech s pomocí metrik vybere úspěšná a neúspěšná videa a upraví podle nich prompt, AI nebude moct upravovat celý prompt ale pouze část kterou určíme

Verze 3
Png charakter v ruznych stylech, který vypráví informace o videu
ElevenLabs
LLM navíc ještě vytváří scénář jako vyprávění o mapě spolu s časováním a reakcí charakteru. 
ElevenLabs vytvoří z textu AI hlas a pomocí ffmpegu udela titulky. 
Dále v této verzi chceme přidat zvyrazneni a zoomování zemí o kterých zrovna mluví a případně nějaké doplňující obrázky a zvuky

Schvalování
GitHub Actions
E-mail
Po vygenerování videa se automaticky odešle e-mail ke schválení
V e-mailu bude odkaz na video a možnosti → schválit, zamítnout, vygenerovat další
Podle odpovědi se automaticky spustí další krok
E-mail bude sloužit jako jednoduché UI, nebude potřeba vytvářet vlastní aplikaci

Cloud
GitHub
GitHub Actions
Python
FFmpeg
Celý projekt bude běžet v cloudu, takže nebude závislý na našich počítačích
Kód bude uložený na GitHubu a GitHub Actions bude automaticky spouštět generování videí
Python se postará o generování skriptu, map a dalších prvků, FFmpeg o výsledné video
Projekt bude přístupný pro oba z různých zařízení a bude možné ho automaticky spouštět 3× denně
