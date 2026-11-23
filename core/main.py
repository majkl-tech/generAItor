import json

from script import vytvor_scenar


def main():
    scenar = vytvor_scenar("Populace evropských zemí")

    # uložit pro další kroky (mapa, FFmpeg...)
    with open("scenar.json", "w", encoding="utf-8") as f:
        json.dump(scenar, f, ensure_ascii=False, indent=2)

    print(scenar["title"])
    for i, scena in enumerate(scenar["scenes"]):
        print(i, scena["text"], scena["duration"])
        # tady navážou další kroky na video


if __name__ == "__main__":
    main()
