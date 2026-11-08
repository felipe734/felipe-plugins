# felipe-plugins

Fuente única de las skills de Felipe OS, el sistema personal de Felipe Tobar. Claude.ai sincroniza este repositorio como marketplace de la organización, junto con `verse-plugins` y `cc-plugins`.

- `plugins/felipe/` — el plugin con las 4 skills de Felipe OS: felipe-os, felipe-trazabilidad, felipe-recurrentes y felipe-gym. Datos personales en la base FELIPE de Airtable (`appJP5HcHMyhPRdcA`).
- Para publicar un cambio: subir la versión en `plugins/felipe/.claude-plugin/plugin.json` y fusionar el PR en `main`.
- Independiente de Verse OS desde el 8 nov 2026. Del plugin `verse` solo usa `os-correo` (lectura del correo personal por Composio).
- Una tarea programada: Felipe OS · Recurrentes (días 28 a 31). Sin brief propio: el brief de Verse lee la base FELIPE en solo lectura para su bloque PERSONAL.
