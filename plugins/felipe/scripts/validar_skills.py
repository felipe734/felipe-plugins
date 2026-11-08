#!/usr/bin/env python3
"""Validador del plugin Felipe (felipe).

Mismas reglas que el validador de Verse, acotadas a Felipe OS: prefijo felipe-, registro con
verse-trazabilidad, sección "Cómo se engrana en Felipe OS", presencia en el catálogo de
felipe-os, correo solo por os-correo/verse-marca, sin secretos, versión subida y conteo
del README. Corre en cada pull request y a mano:

    python3 plugins/felipe/scripts/validar_skills.py [--raiz plugins/felipe] [--base origin/main]

Sale con 1 si hay errores. Las advertencias no bloquean.
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

MODELOS_VALIDOS = {"haiku", "sonnet", "opus"}
PROCESOS_FELIPE = {"Felipe OS", "Felipe recurrentes", "Correo", "Manual"}
SECRETOS = [
    (r"\bpat[A-Za-z0-9]{14}\.[A-Za-z0-9]{20,}", "token de Airtable"),
    (r"\bkey[A-Za-z0-9]{14}\b", "API key de Airtable"),
    (r"\bghp_[A-Za-z0-9]{20,}", "token de GitHub"),
    (r"\bsk-[A-Za-z0-9_-]{20,}", "API key"),
    (r"\bAKIA[0-9A-Z]{16}\b", "clave AWS"),
    (r"-----BEGIN [A-Z ]*PRIVATE KEY-----", "llave privada"),
    (r"\b\d{3}-?\d{6}-?\d{2}\b(?=.*(?:cuenta|ahorros|corriente))", "número de cuenta bancaria"),
]


def frontmatter(texto):
    m = re.match(r"^---\n(.*?)\n---\n", texto, re.S)
    if not m:
        return None
    fm = {}
    for linea in m.group(1).splitlines():
        if ":" in linea and not linea.startswith(" "):
            k, v = linea.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def sin_codigo(texto):
    texto = re.sub(r"```.*?```", "", texto, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", texto)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", default="plugins/felipe")
    ap.add_argument("--base", default=None)
    args = ap.parse_args()
    raiz = Path(args.raiz)
    errores, avisos = [], []

    skills_dir = raiz / "skills"
    skills = sorted(d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists())
    catalogo = (skills_dir / "felipe-os/references/catalogo.md").read_text(encoding="utf-8")

    for d in skills:
        n = d.name
        t = (d / "SKILL.md").read_text(encoding="utf-8")
        fm = frontmatter(t)
        if not fm:
            errores.append(f"{n}: SKILL.md sin frontmatter")
            continue
        modelo = fm.get("model")
        if modelo is not None and modelo not in MODELOS_VALIDOS:
            errores.append(f"{n}: model '{modelo}' no es haiku, sonnet ni opus")
        if modelo is None:
            avisos.append(f"{n}: sin model en el frontmatter")
        if fm.get("name") != n:
            errores.append(f"{n}: frontmatter name='{fm.get('name')}' distinto al directorio")
        if len(fm.get("description", "")) < 40:
            errores.append(f"{n}: description vacía o demasiado corta")
        if not re.match(r"^felipe-[a-z0-9-]+$", n):
            errores.append(f"{n}: nombre sin prefijo felipe-")
        if "## Cómo se engrana en Felipe OS" not in t:
            errores.append(f"{n}: falta la sección 'Cómo se engrana en Felipe OS'")
        if "verse-trazabilidad" not in t:
            errores.append(f"{n}: no registra en TRAZABILIDAD (no menciona verse-trazabilidad)")
        if n not in catalogo:
            errores.append(f"{n}: no está en el catálogo de Felipe OS (catalogo.md)")
        if "mcp__Gmail__" in t:
            errores.append(f"{n}: usa el conector Gmail nativo; el correo va por os-correo y verse-marca")
        for proc in re.findall(r"Proceso `([^`]+)`", t):
            if proc not in PROCESOS_FELIPE:
                avisos.append(f"{n}: Proceso `{proc}` no es un Proceso de Felipe OS en TRAZABILIDAD")
        if re.search(r"[¡!]", sin_codigo(t)):
            avisos.append(f"{n}: signos de admiración en la prosa")
        for extra in d.rglob("*"):
            if extra.is_file() and extra.suffix in {".md", ".py", ".js", ".json", ".html", ".txt"}:
                tx = extra.read_text(encoding="utf-8", errors="ignore")
                for patron, que in SECRETOS:
                    if re.search(patron, tx):
                        errores.append(f"{n}/{extra.relative_to(d)}: parece contener {que}")

    pj = json.loads((raiz / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
    version = pj.get("version", "")
    if not re.match(r"^\d+\.\d+\.\d+$", version):
        errores.append(f"plugin.json: versión inválida '{version}'")
    readme = (raiz / "README.md").read_text(encoding="utf-8")
    m = re.search(r"(\d+) skills?\b", readme)
    if not m or int(m.group(1)) != len(skills):
        errores.append(f"README.md dice {m.group(1) if m else '?'} skills y hay {len(skills)}")
    if args.base:
        try:
            viejo = subprocess.run(["git", "show", f"{args.base}:{raiz}/.claude-plugin/plugin.json"],
                                   capture_output=True, text=True, check=True).stdout
            if json.loads(viejo).get("version") == version:
                errores.append(f"plugin.json: la versión sigue en {version}; hay que subirla")
        except subprocess.CalledProcessError:
            avisos.append("no se pudo leer plugin.json de la base (repositorio nuevo o rama sin base)")

    for a in avisos:
        print("AVISO ", a)
    for e in errores:
        print("ERROR ", e)
    print(f"\n{len(skills)} skills · versión {version} · {len(errores)} errores · {len(avisos)} avisos")
    sys.exit(1 if errores else 0)


if __name__ == "__main__":
    main()
