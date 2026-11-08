# felipe-plugins

Fuente única de las skills de Felipe OS, el sistema personal de Felipe Tobar. Claude.ai sincroniza este repositorio como marketplace de la organización, junto con `verse-plugins` y `cc-plugins`.

- `plugins/felipe/` — el plugin con las 3 skills de Felipe OS: felipe-os, felipe-recurrentes y felipe-gym. Datos personales en la base FELIPE de Airtable (`appJP5HcHMyhPRdcA`).
- Para publicar un cambio: subir la versión en `plugins/felipe/.claude-plugin/plugin.json` y fusionar el PR en `main`.
- Depende del plugin `verse`: `verse-trazabilidad` (registro), `verse-marca` (formato) y `os-correo` (lectura del correo personal por Composio).
- Sin brief propio ni tareas programadas: lo personal sale en el bloque PERSONAL del brief de Verse.
