#!/usr/bin/env bash
# Executa a skill do Codex usando o ambiente Python do vault.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
VENV_PATH="$PROJECT_ROOT/.venv"

if [[ ! -d "$VENV_PATH" ]]; then
  echo "❌ Virtual environment não encontrado em $VENV_PATH"
  echo "Criando..."
  python3 -m venv "$VENV_PATH"
fi

"$VENV_PATH/bin/python" -m pip install -q requests python-frontmatter 2>/dev/null || true
"$VENV_PATH/bin/python" "$SCRIPT_DIR/anki-word-importer.py"
