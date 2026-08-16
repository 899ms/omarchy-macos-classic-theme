#!/usr/bin/env bash
set -euo pipefail

repo_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
destination=${HOME}/.config/omarchy/themes
themes=(macos-classic-light macos-classic-dark)

usage() {
  echo "Usage: ./install.sh [--destination DIR]"
}

while (($#)); do
  case "$1" in
    --destination)
      if (($# < 2)); then
        echo "Error: --destination requires a directory." >&2
        usage >&2
        exit 2
      fi
      destination=$2
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Error: unknown argument: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

mkdir -p -- "$destination"
for theme in "${themes[@]}"; do
  rm -rf -- "$destination/$theme"
  cp -R -- "$repo_dir/$theme" "$destination/$theme"
  echo "Installed $theme"
done

if fc-list : family 2>/dev/null | tr ',' '\n' | grep -Fxiq 'Monaco'; then
  echo "Monaco is available. Apply it with: omarchy font set Monaco"
else
  echo "Monaco is not installed. Install a licensed copy, then run: omarchy font set Monaco"
fi

echo "Choose a variant with: omarchy theme set macos-classic-light"
echo "Or:                    omarchy theme set macos-classic-dark"
