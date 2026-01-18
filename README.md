# Studijní poznámky – generování PDF

Tento repozitář obsahuje studijní poznámky strukturované pro dlouhodobou práci v Obsidianu a současně optimalizované pro export do PDF.

## Generování PDF

Generování PDF souboru se provádí spuštěním skriptu:

    ./_shared/build/build-notes.sh xxx

kde `xxx` je název složky odpovídající konkrétnímu předmětu, ze kterého se PDF generuje, např.:

    ./_shared/build/build-notes.sh 04_OPT

Skript automaticky:
- projde Markdown soubory ve zvolené složce,
- sjednotí je do jednoho dokumentu,
- použije sdílené šablony a styly ze složky `_shared`,
- vytvoří výsledný PDF soubor.

## Struktura repozitáře

- Každá složka předmětu (např. `04_OPT`) obsahuje jednotlivé kapitoly ve formátu Markdown.
- Složka `_shared` obsahuje společné šablony, styly a build skripty.
- Markdown soubory jsou psány tak, aby byly kompatibilní jak s Obsidianem, tak s Pandocem a LaTeXem.

## Licence

Obsah tohoto repozitáře je poskytován pod licencí uvedenou v souboru `LICENSE`, který je součástí repozitáře.

## License
This repository is licensed under the Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International License.

## Poznámka

Soubory jsou koncipovány primárně jako technické studijní texty. Nejedná se o hotová skripta, ale o strukturované poznámky určené k dalšímu rozšiřování a propojování mezi předměty.
