#!/bin/bash
set -e

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
SUBJECT="$1"

YEAR=$(date +"%Y")
AUTHOR="Bc. Jakub Kočí"
SUBJECT_TITLE="$SUBJECT"

export TEXINPUTS="$ROOT/_shared/tul//:"

pandoc \
  --from=markdown-yaml_metadata_block \
  --metadata-file="$ROOT/_shared/metadata/notes.yaml" \
  --metadata subject-title="$SUBJECT_TITLE" \
  --metadata author="$AUTHOR" \
  --metadata year="$YEAR" \
  "$ROOT/$SUBJECT"/*.md \
  --resource-path="$ROOT/$SUBJECT/Graphs:$ROOT/$SUBJECT/Images" \
  --lua-filter="$ROOT/_shared/filters/wikilinks.lua" \
  --lua-filter="$ROOT/_shared/filters/tables.lua" \
  --lua-filter="$ROOT/_shared/filters/remove-hr.lua" \
  --template="$ROOT/_shared/templates/notes.tex" \
  --pdf-engine=xelatex \
  --pdf-engine-opt=--shell-escape \
  -o "$ROOT/$SUBJECT/notes.pdf"
